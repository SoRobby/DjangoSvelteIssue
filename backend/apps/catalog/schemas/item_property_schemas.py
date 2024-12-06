from typing import List, Optional

from apps.catalog.models import ItemProperty, TaxonomyItemFile, TaxonomyItemFileVersion
from apps.properties.schemas import PropertyBasicSchema
from ninja import ModelSchema


class ItemPropertyBasicSchema(ModelSchema):
    property_definition: PropertyBasicSchema

    class Meta:
        model = ItemProperty
        fields = "__all__"
