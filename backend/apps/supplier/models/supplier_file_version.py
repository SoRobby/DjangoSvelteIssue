from apps.core.models import SoftDeletionWithUserModel, UserTrackingModel
from django.db import models

from .supplier_file import SupplierFile


# TODO - MIGRATE TO USING THE ABSTRACT BASE MODEL
# TODO - MIGRATE TO USING THE ABSTRACT BASE MODEL
# TODO - MIGRATE TO USING THE ABSTRACT BASE MODEL
# TODO - MIGRATE TO USING THE ABSTRACT BASE MODEL
class SupplierFileVersion(UserTrackingModel, SoftDeletionWithUserModel):
    supplier_file = models.ForeignKey(SupplierFile, on_delete=models.CASCADE, related_name='versions',
                                      verbose_name='Supplier file',
                                      help_text='Supplier file of the version')

    file = models.FileField(upload_to='supplier/files/', verbose_name='File', help_text='File uploaded by the supplier')

    version = models.PositiveIntegerField(verbose_name='Version', blank=True, help_text='Version of the file')

    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the file')

    class Meta:
        unique_together = ('supplier_file', 'version')
        ordering = ['supplier_file', '-version']
        verbose_name = 'Supplier file version'
        verbose_name_plural = 'Supplier file versions'
        indexes = [
            models.Index(fields=['supplier_file']),
            models.Index(fields=['version']),
        ]

    def save(self, *args, **kwargs):
        if not self.pk:
            # Only set the version number when creating a new version
            last_version = SupplierFileVersion.objects.filter(supplier_file=self.supplier_file).order_by(
                '-version').first()
            self.version = (last_version.version + 1) if last_version else 1
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.supplier_file.supplier.name} - {self.supplier_file.name} - v{self.version}'
