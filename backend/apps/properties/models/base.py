# File location: apps/properties/models/base.py

from django.db import models


class PropertyUnitsBaseModel(models.Model):
    units_prefix = models.CharField(max_length=10, blank=True, null=True, verbose_name='Units prefix',
                                    help_text='Units prefix')

    units_suffix = models.CharField(max_length=10, blank=True, null=True, verbose_name='Units suffix',
                                    help_text='Units suffix')

    class Meta:
        abstract = True
