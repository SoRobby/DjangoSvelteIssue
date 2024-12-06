from django.db import models

from apps.supplier.models import Supplier
from .base import InquiryBaseModel


class SupplierInquiry(InquiryBaseModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='supplier_inquiries', verbose_name='Supplier',
                                 help_text='Supplier of the item inquiry')

    class Meta:
        ordering = ['date_created']
        verbose_name = 'Supplier inquiry'
        verbose_name_plural = 'Supplier inquiries'

    def __str__(self) -> str:
        return f'{self.supplier.name} - Inquiry {self.pk}'
