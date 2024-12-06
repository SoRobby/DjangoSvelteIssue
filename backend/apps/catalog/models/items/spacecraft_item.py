from apps.supplier.models import Supplier
from django.db import models

from ..taxonomy import TaxonomyItem

# TODO - How do you account for multiple suppliers for a single item?
# TODO - How do you account for multiple items for a single product, e.g., F9 Block 1, FK Block 2, etc.?

"""
Model inherits the following fields from TaxonomyItem:
- node (ForeignKey): Node the item is correlated to.
- name (CharField): Name of the item.
- slug (SlugField): The slug based on the item name.
- description (TextField): Description of the item.
- admin_notes (TextField): Internal notes for the admin.
- status (CharField): Status of the node.
- visibility (CharField): Visibility of the item.
"""


class SpaceVehicleItem(TaxonomyItem):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='space_vehicle_details',
                                 verbose_name='Supplier', help_text='Supplier of the space vehicle')

    is_flight_proven = models.BooleanField(default=False, verbose_name='Is flight proven', help_text='Has the item been proven to work in space?')

    class Meta:
        ordering = ['id']
        verbose_name = 'Space vehicle item'
        verbose_name_plural = 'Space vehicle item'

    def __str__(self):
        return f'{self.name}'

    @property
    def dry_mass(self):
        return self.properties.get(key='mass')

        # try:
        #     return self.properties.get(property_reference__slug='mass')
        # except:
        #     return None
