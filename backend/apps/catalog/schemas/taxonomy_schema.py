from typing import List

from apps.catalog.models import Taxonomy
from apps.core.schemas import BaseResponseSchema
from ninja import ModelSchema


# Schemas
class TaxonomyBasicSchema(ModelSchema):
    class Meta:
        model = Taxonomy
        fields = ["name", "slug", "key", "description"]


# Phase out:
class TaxonomySchema(ModelSchema):
    class Meta:
        model = Taxonomy
        fields = ["name", "slug", "key", "description"]


# Get
class GetTaxonomySchema(BaseResponseSchema):
    taxonomy: TaxonomyBasicSchema


class GetTaxonomyListSchema(BaseResponseSchema):
    taxonomies: List[TaxonomyBasicSchema]
