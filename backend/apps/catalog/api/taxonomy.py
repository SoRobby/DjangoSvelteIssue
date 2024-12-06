import logging

from apps.catalog.models import Taxonomy
from apps.catalog.schemas import (
    GetTaxonomyListSchema,
    GetTaxonomySchema,
    TaxonomySchema,
)
from django.http import HttpRequest

from .router import catalog_router


@catalog_router.get("/catalog")
def get_taxonomies(request: HttpRequest):
    logging.debug("[CATALOG.API.GET_CATALOG] Called")
    taxonomies = Taxonomy.objects.all()
    taxonomies_data = [TaxonomySchema.from_orm(taxonomy) for taxonomy in taxonomies]

    return 200, GetTaxonomyListSchema(success=True, taxonomies=taxonomies_data)


@catalog_router.get("/catalog/{taxonomy_slug}")
def get_taxonomy(request: HttpRequest, taxonomy_slug: str):
    logging.debug("[CATALOG.API.GET_TAXONOMY] Called")

    taxonomy = Taxonomy.objects.get(slug=taxonomy_slug)
    taxonomy_data = TaxonomySchema.from_orm(taxonomy)
    
    return 200, GetTaxonomySchema(
            success=True,
            taxonomy=taxonomy_data
        )