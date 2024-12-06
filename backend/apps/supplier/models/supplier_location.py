from apps.core.models import AddressModel, UserTrackingModel
from django.db import models

from .supplier import Supplier


class SupplierLocation(UserTrackingModel, AddressModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='locations', verbose_name='Supplier',
                                 help_text='Supplier of the location')

    # Name for the location (e.g., "New York Office", "London Office")
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Name',
                            help_text='Name of the location')

    # Short description of what the location is or specializes in
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Description',
                                   help_text='Description of the location')

    # Some locations may have a specific website, for example a European vs US website
    website = models.URLField(max_length=255, blank=True, null=True, verbose_name='Website',
                              help_text='Website of the location')
    
    # TODO - Add handling so there is only one headquarters per supplier
    is_headquarters = models.BooleanField(default=False, verbose_name='Is headquarters', help_text='Whether the location is the headquarters of the supplier')

    class Meta:
        ordering = ['address1']
        verbose_name = 'Supplier location'
        verbose_name_plural = 'Supplier locations'

    def __str__(self) -> str:
        _address = self.address1

        if self.address2:
            _address = f'{_address}, {self.address2}'

        _address = f'{_address}, {self.city}, {self.postal_code}'

        if self.is_headquarters:
            _address = f'{_address} (HQ)'

        return str(_address)