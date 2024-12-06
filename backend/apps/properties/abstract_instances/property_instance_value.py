from apps.properties.models import Property
from django.db import models


class PropertyInstanceValue(models.Model):
    property_definition = models.ForeignKey(Property, blank=True, null=True, on_delete=models.SET_NULL,
                                            related_name='%(app_label)s_%(class)s_items',
                                            verbose_name='Property definition',
                                            help_text='Property to assign to the item')
    
    # display_value = models.CharField(max_length=255, blank=True, null=True, verbose_name='Display value',
    #                                  help_text='Display value with units')

    integer_value = models.IntegerField(blank=True, null=True, verbose_name='Integer value',
                                        help_text='Integer value of the property instance')

    float_value = models.FloatField(blank=True, null=True, verbose_name='Float value',
                                    help_text='Float value of the property instance')

    string_value = models.CharField(max_length=255, blank=True, null=True, verbose_name='String value',
                                    help_text='String value of the property instance')

    class Meta:
        abstract = True
