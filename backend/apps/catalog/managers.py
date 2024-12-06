from django.db import models


class TaxonomyItemManager(models.Manager):
    def get_all_properties(self, item_id):
        """ Retrieve all properties of the TaxonomyItem """

        return self.get(id=item_id).properties.all()

    def get_properties_without_group(self, item_id):
        """ Retrieve all properties of the TaxonomyItem that do not belong to any group """
        return self.get(id=item_id).properties.filter(group__isnull=True)

    def get_all_property_groups(self, item_id):
        """ Retrieve all property groups of the TaxonomyItem """
        return self.get(id=item_id).property_groups.all()
