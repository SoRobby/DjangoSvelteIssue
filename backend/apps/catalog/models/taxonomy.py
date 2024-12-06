# File location: apps/catalog/models/taxonomy.py

import re
from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from apps.catalog.managers import TaxonomyItemManager
from apps.core.custom_fields import KeyField
from apps.core.models import SoftDeletionWithUserModel, UserTrackingModel
from apps.properties.models import Property
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

if TYPE_CHECKING:
    from django.db.models import QuerySet


# Models
class Taxonomy(UserTrackingModel):
    class TaxonomyChoices(models.TextChoices):
        SPACECRAFT = 'spacecraft', 'Spacecraft'
        LAUNCH_VEHICLE = 'launch-vehicle', 'Launch Vehicle'
        LAUNCH_SITE = 'launch-site', 'Launch Site'


    name = models.CharField(max_length=255, unique=True, verbose_name='Name', choices=TaxonomyChoices, help_text='Name of the taxonomy')

    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug', help_text='The slug based on the taxonomy name')

    key = KeyField()

    description = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the taxonomy')

    admin_notes = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Admin notes',
                                   help_text='Internal notes for the admin')

    class Meta:
        ordering = ['name']
        verbose_name = 'Taxonomy'
        verbose_name_plural = 'Taxonomies'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
            models.Index(fields=['key'])
        ]


    def save(self, *args, **kwargs):
        if self.name:
            # Ensure slug matches the lowercase form of the name choice value
            self.slug = self.name.lower()

            # Generate a valid key from the slug
            # Replace invalid characters with underscores and ensure the key starts with a valid character
            self.key = self.slug.replace('-', '_').replace(' ', '_')
            if not self.key[0].isalpha():
                self.key = f"_{self.key}"

        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    

class TaxonomyNode(UserTrackingModel):
    # TODO maybe add a node path to the root node?
    class StatusChoices(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'

    taxonomy = models.ForeignKey(Taxonomy, on_delete=models.CASCADE, related_name='nodes',
                                 verbose_name='Taxonomy', help_text='Taxonomy to assign nodes to')

    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children',
                               verbose_name='Parent node', help_text='Parent node of the node')
    
    children: "QuerySet[TaxonomyNode]"
    
    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the node')

    slug = models.SlugField(max_length=255, verbose_name='Slug', help_text='The slug based on the node name')

    key = KeyField()

    description = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the node')

    status = models.CharField(max_length=12, choices=StatusChoices.choices, default=StatusChoices.PUBLISHED,
                              verbose_name='Status', help_text='Status of the node')

    weight = models.DecimalField(
        max_digits=3, decimal_places=2, default=0.5, verbose_name='Weight',
        help_text='Weight of the node, value between 0 and 1 with two decimals',
        validators=[
            MinValueValidator(0, message='The weight must be between 0 and 1'),
            MaxValueValidator(1, message='The weight must be between 0 and 1')
        ]
    )

    admin_notes = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Admin notes',
                                   help_text='Internal notes for the admin')

    class Meta:
        ordering = ['name']
        verbose_name = 'Taxonomy node'
        verbose_name_plural = 'Taxonomy nodes'
        constraints = [
            models.UniqueConstraint(fields=['taxonomy', 'slug'], name='unique_taxonomy_slug')
        ]
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
            models.Index(fields=['key'])
        ]

    def __str__(self):
        return f'{self.taxonomy.name} - {self.name} (id={self.pk})'

    def clean(self):
        if self.parent == self:
            raise ValidationError('A node cannot be its own parent.')

        if self._is_circular_reference():
            raise ValidationError('Circular reference detected. A node cannot be its own ancestor.')

        if self.parent and self.parent.taxonomy != self.taxonomy:
            raise ValidationError('Parent node must belong to the same taxonomy.')

    def _is_circular_reference(self):
        """
        Checks for circular references to prevent a node from being an ancestor of itself.
        """
        current_node = self.parent
        while current_node is not None:
            if current_node == self:
                return True
            current_node = current_node.parent
        return False

    def save(self, *args, **kwargs):
        if self.key:
            self.key = re.sub('[^a-z0-9_]', '', self.key.lower())

        self.clean()
        super().save(*args, **kwargs)


class TaxonomyNodeAlternativeName(UserTrackingModel):
    node = models.ForeignKey(TaxonomyNode, on_delete=models.CASCADE, related_name='alternative_names',
                             verbose_name='Node', help_text='Node to assign alternative names to')

    name = models.CharField(max_length=255, verbose_name='Name', help_text='Alternative name of the node')

    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the alternative name')

    admin_notes = models.TextField(max_length=2000, blank=True, null=True, verbose_name='Admin notes',
                                   help_text='Internal notes for the admin')

    class Meta:
        ordering = ['name']
        verbose_name = 'Taxonomy node alternative name'
        verbose_name_plural = 'Taxonomy node alternative names'
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name


class TaxonomyItem(UserTrackingModel, SoftDeletionWithUserModel):
    class StatusChoices(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'

    class VisibilityChoices(models.TextChoices):
        NORMAL = 'normal', 'Normal'
        HIDDEN = 'hidden', 'Hidden'
        ADMIN = 'admin', 'Admin'
    
    # New: Added this because nodes can be deleted, but the items themselves should not be deleted and should still remain
    # within the taxonomy.
    taxonomy_object = models.ForeignKey('Taxonomy', on_delete=models.CASCADE, related_name='items', 
                                        verbose_name='Taxonomy', help_text='Taxonomy the item resides under')

    node = models.ForeignKey(TaxonomyNode, blank=True, null=True, on_delete=models.SET_NULL,
                             related_name='items', verbose_name='Node',
                             help_text='Node the item is correlated to')

    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the item')

    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug',
                            help_text='The slug based on the item name')

    description = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the item')

    status = models.CharField(max_length=12, choices=StatusChoices.choices, default=StatusChoices.PUBLISHED,
                              verbose_name='Status', help_text='Status of the node')

    visibility = models.CharField(max_length=12, choices=VisibilityChoices.choices, default=VisibilityChoices.NORMAL,
                                  verbose_name='Visibility', help_text='Visibility of the node')

    cached_properties = models.JSONField(blank=True, null=True, verbose_name='Cached properties',
                                         help_text='Cached properties for the item')

    api_allowed = models.BooleanField(default=True, verbose_name='Allow API access',
                                      help_text='Allow access to the item via the API')

    admin_notes = models.TextField(max_length=5000, blank=True, null=True, verbose_name='Admin notes',
                                   help_text='Internal notes for the admin')

    objects = TaxonomyItemManager()

    class Meta:
        ordering = ['name']
        verbose_name = 'Taxonomy item'
        verbose_name_plural = 'Taxonomy items'
        indexes = [
            models.Index(fields=['node']),
            models.Index(fields=['name']),
            models.Index(fields=['slug'])
        ]

    def __str__(self):
        if self.node:
            return f'{self.node.taxonomy.name} - {self.name} ({self.pk})'
        else:
            return f'{self.name} ({self.pk})'

    # TODO - Maybe each item should have a unique slug that is unique within the taxonomy?
    def save(self, *args, **kwargs):
        if self.node and self.slug:
            taxonomy = self.node.taxonomy
            if TaxonomyItem.objects.filter(slug=self.slug, node__taxonomy=taxonomy).exclude(pk=self.pk).exists():
                raise ValidationError(f"The slug '{self.slug}' already exists in the taxonomy '{taxonomy.name}'.")
        super().save(*args, **kwargs)


    @property
    def taxonomy(self):
        if self.node:
            return self.node.taxonomy
        return None
