# File location: apps/properties/models/property_set.py

from django.core.validators import RegexValidator
from django.db import models
from .property import Property

from apps.core.models import UserTrackingModel
from apps.core.custom_fields import KeyField

class PropertySet(UserTrackingModel):
    """
    Fields removed:
    - Slug filed was removed from the model as it was not needed and I did not see a use case for it.
    - Status field was removed from the model as it was not needed and I did not see a use case for it. Additionally
    the status field is used on the "Property" model and it was redundant to have it on this model as well.
    """
    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the property')

    key = KeyField()

    properties = models.ManyToManyField(Property, related_name='property_sets', verbose_name='Properties',
                                        help_text='Properties to assign to the set')

    description = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the property')

    admin_notes = models.TextField(max_length=5000, blank=True, null=True, verbose_name='Admin notes',
                                   help_text='Internal notes for the admin')

    class Meta:
        ordering = ['name']
        verbose_name = 'Property set'
        verbose_name_plural = 'Property sets'
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
        return self.name
