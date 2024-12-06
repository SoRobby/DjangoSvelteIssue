from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

from apps.core.models import UserTrackingModel
from apps.properties.models.base import PropertyUnitsBaseModel


def check_existing_property_types(property_instance, excluding_type):
    linked_types = ['float_property', 'integer_property']
    if excluding_type:
        linked_types.remove(excluding_type)

    if any(hasattr(property_instance, attr) for attr in linked_types):
        raise ValidationError(f"A different property type is already linked to this Property.")


class Property(UserTrackingModel):
    class StatusChoices(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'

    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the property')

    slug = models.SlugField(max_length=255, verbose_name='Slug', help_text='Unique slug of the property')

    key = models.CharField(max_length=255, verbose_name='Key', help_text='Key of the property, used for API calls',
                           validators=[RegexValidator(regex='^[a-z_][a-z0-9_]*$',
                                                      message='Key must be lowercase, cannot start with a number, and\
                                                      can only contain underscores.')])

    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PUBLISHED,
                              verbose_name='Status', help_text='Status of the node')

    description = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the property')

    admin_notes = models.TextField(max_length=5000, blank=True, null=True, verbose_name='Admin notes',
                                   help_text='Internal notes for the admin')


    class Meta:
        ordering = ['name']
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class IntegerProperty(PropertyUnitsBaseModel, UserTrackingModel):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='integer_property',
                                    verbose_name='Property', help_text='Property to assign to the item')

    default_value = models.IntegerField(verbose_name='Default value', help_text='Default value of the property')

    is_min_limit_enabled = models.BooleanField(default=False, verbose_name='Is min limit enabled',
                                               help_text='Whether the minimum limit is enabled or not')

    is_max_limit_enabled = models.BooleanField(default=False, verbose_name='Is max limit enabled',
                                               help_text='Whether the maximum limit is enabled or not')

    min_limit_value = models.IntegerField(blank=True, null=True, verbose_name='Min limit value',
                                          help_text='Minimum limit value of the property')

    max_limit_value = models.IntegerField(blank=True, null=True, verbose_name='Max limit value',
                                          help_text='Maximum limit value of the property')

    class Meta:
        verbose_name = 'Integer property'
        verbose_name_plural = 'Integer properties'


    def clean(self):
        check_existing_property_types(self.property, 'integer_property')
        super().clean()


class FloatProperty(PropertyUnitsBaseModel, UserTrackingModel):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='float_property',
                                    verbose_name='Property', help_text='Property to assign to the item')

    default_value = models.FloatField(verbose_name='Default value', help_text='Default value of the property')

    step_size = models.PositiveIntegerField(default=1, verbose_name='Step size', help_text='Step size of the property')

    is_min_limit_enabled = models.BooleanField(default=False, verbose_name='Is min limit enabled',
                                               help_text='Whether the minimum limit is enabled or not')

    is_max_limit_enabled = models.BooleanField(default=False, verbose_name='Is max limit enabled',
                                               help_text='Whether the maximum limit is enabled or not')

    min_limit_value = models.FloatField(blank=True, null=True, verbose_name='Min limit value',
                                        help_text='Minimum limit value of the property')

    max_limit_value = models.FloatField(blank=True, null=True, verbose_name='Max limit value',
                                        help_text='Maximum limit value of the property')

    class Meta:
        verbose_name = 'Float property'
        verbose_name_plural = 'Float properties'

    def clean(self):
        check_existing_property_types(self.property, 'float_property')
        super().clean()

