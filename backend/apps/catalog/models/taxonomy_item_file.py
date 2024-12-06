from apps.core.models import SoftDeletionWithUserModel, UserTrackingModel
from apps.core.models.abstracts import BaseFileModel
from django.db import models

from .taxonomy import TaxonomyItem


class TaxonomyItemFile(BaseFileModel, UserTrackingModel, SoftDeletionWithUserModel):
    item = models.ForeignKey(TaxonomyItem, on_delete=models.CASCADE, related_name='files', verbose_name='Item',
                                 help_text='Taxonomy item of the file')

    class Meta:
        ordering = ['item', 'name']
        verbose_name = 'Taxonomy item file'
        verbose_name_plural = 'Taxonomy item files'

    def __str__(self) -> str:
        return f'{self.item.name} - {self.name}'
    
