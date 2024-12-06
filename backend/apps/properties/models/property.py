from apps.core.custom_fields import KeyField
from apps.core.models import UserTrackingModel
from apps.properties.managers import BuiltinPropertyManager, CustomPropertyManager
from django.core.validators import RegexValidator
from django.db import models

from .property_library import PropertyLibrary

'''
Future options to evaluate and potentially change:
1. OneToOne relationship with model validation (currently what is implemented)
2. Use Generic Foreign Key to link the property to the property type
3. Use polymorphic model-relationship to link the property to the property type
'''


class Property(UserTrackingModel):
    class PropertyTypeChoices(models.TextChoices):
        INTEGER = 'integer', 'Integer'
        FLOAT = 'float', 'Float'
        STRING = 'string', 'String'
        BOOLEAN = 'boolean', 'Boolean'

    class StatusChoices(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'

    library = models.ForeignKey(PropertyLibrary, on_delete=models.CASCADE, related_name='properties',
                                verbose_name='Library', help_text='Library to assign the property to')

    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the property')

    slug = models.SlugField(max_length=255, verbose_name='Slug', help_text='Unique slug of the property')

    key = KeyField()

    property_type = models.CharField(max_length=20, choices=PropertyTypeChoices.choices, verbose_name='Property type',
                                     help_text='Type of the property')

    is_builtin = models.BooleanField(default=False, verbose_name='Is built-in',
                                     help_text='Whether the property is built-in or not')

    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PUBLISHED,
                              verbose_name='Status', help_text='Status of the node')

    description = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the property')

    admin_notes = models.TextField(max_length=5000, blank=True, null=True, verbose_name='Admin notes',
                                   help_text='Internal notes for the admin')

    class Meta:
        ordering = ['name']
        unique_together = ['library', 'slug']
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
        indexes = [
            models.Index(fields=['library']),
            models.Index(fields=['slug']),
            models.Index(fields=['key']),
        ]

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if self.is_builtin != self.library.is_builtin:
            self.is_builtin = self.library.is_builtin

        # Check to make sure property value is of same type
        # Check to make sure the child property value (e.g., IntegerProperty, FloatProperty, etc...) is
        # TODO - Maybe look at what I am doing with teh catalog items and launch vehicle items.

        super().save(*args, **kwargs)

    @property
    def typed_property(self):
        return getattr(self, f'{self.property_type}_property', None)

    @property
    def property_value(self):
        if hasattr(self, 'integer_property'):
            return self.integer_property
        elif hasattr(self, 'float_property'):
            return self.float_property
        elif hasattr(self, 'string_property'):
            return self.string_property

        # Add more conditions for other property types
        else:
            return None


class BuiltinProperty(Property):
    objects = BuiltinPropertyManager()

    class Meta:
        proxy = True
        verbose_name = 'Builtin property'
        verbose_name_plural = 'Builtin properties'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class CustomProperty(Property):
    objects = CustomPropertyManager()

    class Meta:
        proxy = True
        verbose_name = 'Custom property'
        verbose_name_plural = 'Custom properties'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
