import json
import logging
import time
from collections import defaultdict
from typing import List, Optional

from apps.catalog.models import SpaceVehicleItem, Taxonomy, TaxonomyItem, TaxonomyNode
from apps.catalog.schemas import (
    GetTaxonomyNodeListSchema,
    GetTaxonomyNodeListWithChildrenSchema,
    GetTaxonomyNodeNestedListSchema,
    NestedTaxonomyNodeSchema,
    SpaceVehicleItemBasicSchema,
    SpaceVehicleItemDetailedSchema,
    TaxonomyItemSimpleSchema,
    TaxonomyNodeSchema,
    TaxonomyNodeWithChildrenSchema,
)
from apps.core.schemas import BaseResponseSchema
from apps.supplier.models import Supplier
from apps.supplier.schemas import SupplierBasicSchema
from django.db.models import Count, Prefetch
from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from ninja import ModelSchema, Query, Schema
from pydantic import BaseModel

from .router import catalog_router


@catalog_router.get("/catalog/{taxonomy_slug}/detail/{item_slug}")
def get_taxonomy_item(request: HttpRequest, taxonomy_slug: str, item_slug: str):
    """
    Root views will not return items, only new views will return items.
    """
    logging.debug("[CATALOG.API] get_taxonomy_item() Called")

    # Identify the type of taxonomy
    if taxonomy_slug == Taxonomy.TaxonomyChoices.SPACECRAFT:
        item = SpaceVehicleItem.objects.get(slug=item_slug)

        print(f"item = {item}")
        

        item = SpaceVehicleItemDetailedSchema.from_orm(item)





    if taxonomy_slug == Taxonomy.TaxonomyChoices.LAUNCH_SITE:
        pass

    if taxonomy_slug == Taxonomy.TaxonomyChoices.LAUNCH_VEHICLE:
        pass

    else:
        pass

    
    return 200, BaseResponseSchema(
            success=True,
            message="Request was successful",
            item=item # type: ignore
        )
