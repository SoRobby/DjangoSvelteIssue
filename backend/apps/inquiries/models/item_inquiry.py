from django.db import models

from apps.catalog.models import TaxonomyItem
from apps.supplier.models import Supplier
from .base import InquiryBaseModel


class ItemInquiry(InquiryBaseModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='item_inquiries', verbose_name='Supplier',
                                 help_text='Supplier of the item inquiry')

    item = models.ForeignKey(TaxonomyItem, on_delete=models.SET_NULL, blank=True, null=True,
                             related_name='item_inquiries', verbose_name='Item', help_text='Item of the inquiry')

    request_datasheet = models.BooleanField(default=False, verbose_name='Request datasheet',
                                            help_text='Request datasheet of the item')

    request_icd = models.BooleanField(default=False, verbose_name='Request ICD', help_text='Request ICD of the item')

    request_options_sheet = models.BooleanField(default=False, verbose_name='Request options sheet',
                                                help_text='Request options sheet of the item')

    request_user_manual = models.BooleanField(default=False, verbose_name='Request user manual',
                                              help_text='Request user manual of the item')

    request_cad_model = models.BooleanField(default=False, verbose_name='Request CAD model',
                                            help_text='Request CAD model of the item')

    request_quotation = models.BooleanField(default=False, verbose_name='Request quotation',
                                            help_text='Request quotation of the item')

    request_lead_time = models.BooleanField(default=False, verbose_name='Request lead time',
                                            help_text='Request lead time of the item')

    request_heritage = models.BooleanField(default=False, verbose_name='Request heritage',
                                           help_text='Request heritage of the item')

    number_of_flight_units = models.PositiveIntegerField(verbose_name='Number of flight units', blank=True, null=True,
                                                         help_text='Number of flight units of the item')

    number_of_engineering_units = models.PositiveIntegerField(verbose_name='Number of engineering units', blank=True,
                                                              null=True,
                                                              help_text='Number of engineering units of the item')

    class Meta:
        ordering = ['date_created']
        verbose_name = 'Item inquiry'
        verbose_name_plural = 'Item inquiries'

    def __str__(self) -> str:
        if self.item:
            return f'{self.item.name} - Inquiry {self.pk}'
        else:
            return f'Unknown Item Inquiry {self.pk}'
