from typing import List, Optional

from apps.catalog.models import TaxonomyNode, TaxonomyNodeAlternativeName
from apps.core.schemas import BaseResponseSchema
from ninja import ModelSchema
from pydantic import BaseModel


# Root schemas
class TaxonomyNodeAlternativeNameSchema(ModelSchema):
    class Meta:
        model = TaxonomyNodeAlternativeName
        fields = ["name", "node", "description"]


class TaxonomyNodeSchema(ModelSchema):
    class Meta:
        model = TaxonomyNode
        fields = ["name", "slug", "key", "status", "weight", "description"]


class NestedTaxonomyNodeSchema(ModelSchema):
    children: Optional[List["NestedTaxonomyNodeSchema"]] = None

    class Meta:
        model = TaxonomyNode
        fields = ["name", "slug", "key", "status", "weight", "description"]


# Responses
class GetTaxonomyNodeListSchema(BaseResponseSchema):
    nodes: List[TaxonomyNodeSchema]


class GetTaxonomyNodeNestedListSchema(BaseResponseSchema):
    nodes: List[NestedTaxonomyNodeSchema]


class TaxonomyNodeWithChildrenSchema(BaseModel):
    node: TaxonomyNodeSchema
    children: List[TaxonomyNodeSchema]


class GetTaxonomyNodeListWithChildrenSchema(BaseResponseSchema):
    nodes: List[TaxonomyNodeWithChildrenSchema]


