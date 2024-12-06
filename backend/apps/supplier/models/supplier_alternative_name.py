from django.db import models

from apps.core.models import UserTrackingModel
from .supplier import Supplier


class SupplierAlternativeName(UserTrackingModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='alternative_names',
                                 verbose_name='Supplier', help_text='Supplier of the alternative name')

    name = models.CharField(max_length=255, verbose_name='Name', help_text='Alternative name of the supplier')

    class Meta:
        ordering = ['name']
        verbose_name = 'Supplier alternative name'
        verbose_name_plural = 'Supplier alternative names'

    def __str__(self) -> str:
        return f'{self.supplier.name} - {self.name}'
