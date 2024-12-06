# Item location: apps/catalog/models/item_properties.py

from apps.core.custom_fields import KeyField
from apps.core.models import SoftDeletionWithUserModel, UserTrackingModel
from apps.properties.abstract_instances import PropertyInstanceValue
from apps.properties.models import Property
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

from .taxonomy import TaxonomyItem


class ItemPropertyGroup(UserTrackingModel, SoftDeletionWithUserModel):
    item = models.ForeignKey(TaxonomyItem, on_delete=models.CASCADE, related_name='property_groups',
                             verbose_name='Item', help_text='Item to assign the property group to')

    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the property group')

    description = models.TextField(max_length=6000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the property instance group')

    order = models.PositiveIntegerField(default=0, verbose_name='Order', help_text='Order of the property group')

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Item property group'
        verbose_name_plural = 'Item property groups'

    def __str__(self):
        return f'{self.item.node.taxonomy.name} - {self.item.name} - {self.name} ({self.id})'


class ItemProperty(UserTrackingModel, SoftDeletionWithUserModel, PropertyInstanceValue):
    item = models.ForeignKey(TaxonomyItem, on_delete=models.CASCADE, related_name='properties', verbose_name='Item',
                             help_text='Item to assign the property to')

    group = models.ForeignKey(ItemPropertyGroup, blank=True, null=True, on_delete=models.SET_NULL,
                              related_name='group_properties',
                              verbose_name='Group',
                              help_text='Group to assign the property instance to')

    custom_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Custom name',
                                   help_text='Custom name of the property instance')

    custom_key = KeyField(blank=True, null=True, verbose_name='Custom key')

    order = models.PositiveIntegerField(default=0, verbose_name='Order', help_text='Order of the property instance')

    note = models.TextField(max_length=4000, blank=True, null=True, verbose_name='Note', help_text='Note of the property instance')

    class Meta:
        ordering = ['order']
        unique_together = ['item', 'property_definition']
        verbose_name = 'Item property'
        verbose_name_plural = 'Item properties'
        indexes = [
            models.Index(fields=['item', 'property_definition']),
            models.Index(fields=['custom_key'])
        ]

    def __str__(self):
        return f'{self.item.node.taxonomy.name} - {self.item.name} - {self.name} ({self.pk})'

    def clean(self):
        if self.group:
            if self.item != self.group.item:
                raise ValidationError('The Item and Group Item must have the same Item.')
        super().clean()

    def save(self, *args, **kwargs):
        print('Saving property...')

        if self.property_definition and self.property_definition.property_type == Property.PropertyTypeChoices.FLOAT:
            display_value = ''
            if self.property_definition.property_value and self.property_definition.property_value.units_prefix:
                display_value += self.property_definition.property_value.units_prefix
            
            if self.float_value:
                display_value += str(self.float_value)

            if self.property_definition.property_value and self.property_definition.property_value.units_suffix:
                display_value += f' {self.property_definition.property_value.units_suffix}'
           
            self.display_value = display_value
        
        super().save(*args, **kwargs)


