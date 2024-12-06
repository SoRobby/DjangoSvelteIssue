# File location: apps/properties/models/property_types.py

from apps.core.models import UserTrackingModel
from django.core.exceptions import ValidationError
from django.db import models

from .base import PropertyUnitsBaseModel
from .property import Property


def check_existing_property_types(property_instance, excluding_type):
    linked_types = ['integer_property', 'float_property', 'string_property']

    if excluding_type:
        linked_types.remove(excluding_type)

    if any(hasattr(property_instance, attr) for attr in linked_types):
        raise ValidationError(
            f'A different property type is already linked to the Property of "{property_instance.name}".')


def verify_property_type(property_instance, property_type: str):
    if property_instance.property_type != property_type:
        raise ValidationError(f'The property type of "{property_instance.name}" is not a {property_type} type.')


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
        ordering = ['property__name']
        verbose_name = 'Integer property'
        verbose_name_plural = 'Integer properties'

    def __str__(self):
        return f'{self.property.name}'

    def clean(self):
        check_existing_property_types(self.property, 'integer_property')
        verify_property_type(self.property, 'integer')

        # TODO - May want to remove limits or add a box to enforce limits or not. Rationale for the change is
        # that in a design tool you may want to have a limit but not enforce it. Plus if a value is outside the range
        # you may want to show a warning but not prevent the user from saving the value.
        if self.is_min_limit_enabled:
            if self.default_value < self.min_limit_value:
                raise ValidationError('The default value cannot be less than the minimum limit value.')

        if self.is_max_limit_enabled:
            if self.default_value > self.max_limit_value:
                raise ValidationError('The default value cannot be greater than the maximum limit value.')

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
        ordering = ['property__name']
        verbose_name = 'Float property'
        verbose_name_plural = 'Float properties'

    def __str__(self):
        return f'{self.property.name}'

    def clean(self):
        check_existing_property_types(self.property, 'float_property')
        verify_property_type(self.property, 'float')

        if self.is_min_limit_enabled:
            if self.default_value < self.min_limit_value:
                raise ValidationError('The default value cannot be less than the minimum limit value.')

        if self.is_max_limit_enabled:
            if self.default_value > self.max_limit_value:
                raise ValidationError('The default value cannot be greater than the maximum limit value.')

        super().clean()


class StringProperty(UserTrackingModel):
    property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='string_property',
                                    verbose_name='Property', help_text='Property to assign to the item')

    default_value = models.CharField(max_length=255, verbose_name='Default value', blank=True,
                                     help_text='Default value of the property')

    class Meta:
        ordering = ['property__name']
        verbose_name = 'String property'
        verbose_name_plural = 'String properties'

    def __str__(self):
        return f'{self.property.name}'

    def clean(self):
        check_existing_property_types(self.property, 'string_property')
        verify_property_type(self.property, 'string')
        super().clean()

# class BooleanProperty(UserTrackingModel):
#     # TODO - Questions, do I want to allow None as a default value?
#     # TODO - Is has_heritage considered a property or should it be added directory to the satellite parts models?
#     property = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='boolean_property',
#                                     verbose_name='Property', help_text='Property to assign to the item')
#
#     default_value = models.BooleanField(verbose_name='Default value', help_text='Default value of the property')
#
#     class Meta:
#         ordering = ['property__name']
#         verbose_name = 'Boolean property'
#         verbose_name_plural = 'Boolean properties'
#
#     def __str__(self):
#         return f'{self.property.name}'
#
#     def clean(self):
#         check_existing_property_types(self.property, 'boolean_property')
#         super().clean()
