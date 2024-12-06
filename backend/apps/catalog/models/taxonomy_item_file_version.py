from apps.core.models import SoftDeletionWithUserModel, UserTrackingModel
from apps.core.models.abstracts import BaseFileVersionModel
from django.db import models

from .taxonomy_item_file import TaxonomyItemFile


class TaxonomyItemFileVersion(BaseFileVersionModel, UserTrackingModel, SoftDeletionWithUserModel):
    taxonomy_item_file = models.ForeignKey(TaxonomyItemFile, on_delete=models.CASCADE, related_name='versions',
                                      verbose_name='Taxonomy item file',
                                      help_text='Taxonomy item file of the version')

    file = models.FileField(upload_to='taxonomy/files/', verbose_name='File', help_text='File uploaded by a user for a taxonomy item')

    class Meta:
        unique_together = ('taxonomy_item_file', 'version')
        ordering = ['taxonomy_item_file', '-version']
        verbose_name = 'Taxonomy item file version'
        verbose_name_plural = 'Taxonomy item file versions'
        indexes = [
            models.Index(fields=['taxonomy_item_file']),
            models.Index(fields=['version']),
        ]
  
    def __str__(self) -> str:
        return f'{self.taxonomy_item_file.item.name} - {self.taxonomy_item_file.name} - v{self.version}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @property
    def file_field(self):
        return 'taxonomy_item_file'
    

