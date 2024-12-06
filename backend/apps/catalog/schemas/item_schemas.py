from typing import List, Optional

from apps.catalog.models import SpaceVehicleItem, TaxonomyItem
from apps.supplier.schemas import SupplierBasicSchema
from ninja import ModelSchema

from .item_file_schema import TaxonomyItemFileSchema
from .item_property_schemas import ItemPropertyBasicSchema
from .node_schema import TaxonomyNodeSchema
from .taxonomy_schema import TaxonomyBasicSchema


# Phase out...
class TaxonomyItemSimpleSchema(ModelSchema):
    files: Optional[List[TaxonomyItemFileSchema]] = None

    class Meta:
        model = TaxonomyItem
        fields = ["name", "slug", "date_created", "date_modified"]


class TaxonomyItemBasicSchema(ModelSchema):
    files: Optional[List[TaxonomyItemFileSchema]] = None

    class Meta:
        model = TaxonomyItem
        fields = ["name", "slug", "date_created", "date_modified"]


class SpaceVehicleItemBasicSchema(ModelSchema):
    supplier: Optional[SupplierBasicSchema] = None

    class Meta:
        model = SpaceVehicleItem
        fields = ["name", "slug", "date_created", "date_modified", "is_flight_proven"]


class SpaceVehicleItemDetailedSchema(ModelSchema):
    files: Optional[List[TaxonomyItemFileSchema]] = None
    taxonomy: TaxonomyBasicSchema
    node: TaxonomyNodeSchema
    supplier: Optional[SupplierBasicSchema] = None
    properties: Optional[List[ItemPropertyBasicSchema]] = None

    class Meta:
        model = SpaceVehicleItem
        fields = "__all__"
