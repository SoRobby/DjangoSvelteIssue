from ..taxonomy import TaxonomyItem


class LaunchVehicleItem(TaxonomyItem):
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

    class Meta:
        ordering = ['id']
        verbose_name = 'Launch vehicle item'
        verbose_name_plural = 'Launch vehicle items'

    def __str__(self):
        return f'{self.pk}'
