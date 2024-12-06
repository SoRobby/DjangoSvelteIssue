# File location: apps/properties/models/property_alternative_name.py

from django.db import models
from apps.core.models import UserTrackingModel
from .property import Property


class PropertyAlternativeName(UserTrackingModel):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='alternative_names',
                                 verbose_name='Property', help_text='Property to assign to the item')

    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the property')

    description = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the property')

    admin_notes = models.TextField(max_length=5000, blank=True, null=True, verbose_name='Admin notes',
                                   help_text='Internal notes for the admin')

    class Meta:
        ordering = ['name']
        verbose_name = 'Property alternative name'
        verbose_name_plural = 'Property alternative names'
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name
