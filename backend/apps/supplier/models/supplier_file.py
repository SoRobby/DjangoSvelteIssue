from apps.core.models import SoftDeletionWithUserModel, UserTrackingModel
from django.db import models

from .supplier import Supplier


# TODO - MIGRATE TO USING THE ABSTRACT BASE MODEL
# TODO - MIGRATE TO USING THE ABSTRACT BASE MODEL
# TODO - MIGRATE TO USING THE ABSTRACT BASE MODEL
# TODO - MIGRATE TO USING THE ABSTRACT BASE MODEL
class SupplierFile(UserTrackingModel, SoftDeletionWithUserModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='files', verbose_name='Supplier',
                                 help_text='Supplier of the file')

    name = models.CharField(max_length=255, verbose_name='Name', help_text='Name of the file')

    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the file')

    class Meta:
        ordering = ['supplier', 'name']
        verbose_name = 'Supplier file'
        verbose_name_plural = 'Supplier files'

    def __str__(self) -> str:
        return f'{self.supplier.name} - {self.name}'

    @property
    def latest_version(self):
        return self.versions.order_by('-version').first()
