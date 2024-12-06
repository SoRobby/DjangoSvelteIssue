import json
import logging
from typing import List, Optional

from apps.core.models import Country
from apps.core.schemas import BaseResponseSchema, CountryBasicSchema, ErrorSchema
from apps.supplier.models import Supplier, SupplierLocation
from apps.supplier.schemas import (
    SupplierBasicSchema,
    SupplierDetailedSchema,
    SupplierLocationBasicSchema,
    SupplierUpdateSeoSchema,
)
from django.http import HttpRequest
from ninja import Query
from ninja.pagination import LimitOffsetPagination, PageNumberPagination, paginate

from .router import supplier_router

# from django.shortcuts import get_object_or_404
# from ninja.responses import Response
# class SupplierPagination(PageNumberPagination):
#     page_size = 2


# @supplier_router.get("/suppliers", response=List[SupplierBasicSchema])
# @paginate(SupplierPagination)
# def get_suppliers(request: HttpRequest):
#     logging.debug("[SUPPLIER.API.GET_SUPPLIERS] Called")

#     # Get user
#     user = request.user

#     # Get suppliers that are not blocked in the user's country
#     if user.is_authenticated:
#         suppliers = Supplier.objects.exclude(blocked_countries=user.country)
#         logging.debug(f'[SUPPLIER.API.GET_SUPPLIERS] User is authenticated. User country: {user.country}')
#     else:
#         suppliers = Supplier.objects.all()

#     return suppliers


@supplier_router.get("/suppliers")
def get_suppliers(
    request: HttpRequest,
    page: int = Query(1, alias="page"),
    limit: int = Query(1, alias="limit"),
    countries: Optional[List[str]] = Query(None, alias="countries"),
):
    logging.debug("[SUPPLIER.API.GET_SUPPLIERS] Called")

    if page < 1:
        page = 1
    if limit < 1:
        limit = 1

    user = request.user

    if user.is_authenticated:
        suppliers_all = Supplier.objects.exclude(blocked_countries=user.country)
    else:
        suppliers_all = Supplier.objects.all()

    # Apply country filter if provided
    if countries:
        suppliers_filtered = suppliers_all.filter(locations__country__slug__in=countries).distinct()
    else:
        suppliers_filtered = suppliers_all

    # Extract distinct countries for filters
    country_ids = (
        SupplierLocation.objects.filter(supplier__in=suppliers_all).values_list("country_id", flat=True).distinct()
    )
    countries_available = Country.objects.filter(id__in=country_ids).distinct()
    serialized_countries = [CountryBasicSchema.from_orm(country) for country in countries_available]

    # Pagination
    start_index = (page - 1) * limit
    end_index = start_index + limit
    paginated_suppliers = suppliers_filtered[start_index:end_index]

    pagination_data = {
        "page": page,
        "limit": limit,
        "total": suppliers_filtered.count(),
    }

    filter_data = {
        "locations": serialized_countries,
        "tags": [],
    }

    suppliers_data = [SupplierBasicSchema.from_orm(supplier) for supplier in paginated_suppliers]

    return 200, BaseResponseSchema(
        success=True, suppliers=suppliers_data, pagination=pagination_data, filter=filter_data
    )


# @supplier_router.get("/suppliers")
# def get_suppliers(request: HttpRequest):
#     logging.debug("[SUPPLIER.API.GET_SUPPLIERS] Called")

#     # Get user
#     user = request.user

#     # Get suppliers that are not blocked in the user's country
#     if user.is_authenticated:
#         suppliers = Supplier.objects.exclude(blocked_countries=user.country)
#         logging.debug(f'[SUPPLIER.API.GET_SUPPLIERS] User is authenticated. User country: {user.country}')
#     else:
#         suppliers = Supplier.objects.all()

#     # Serialize the suppliers
#     suppliers_data = [SupplierBasicSchema.from_orm(supplier) for supplier in suppliers]

#     return 200, BaseResponseSchema(success=True, suppliers=suppliers_data)  # type: ignore


@supplier_router.get("/suppliers/{supplier_slug}")
def get_supplier(request: HttpRequest, supplier_slug: str):
    logging.debug("[SUPPLIER.API.GET_SUPPLIER] Called")

    # Get user
    user = request.user

    # Get supplier
    supplier = Supplier.objects.get(slug=supplier_slug)

    # If user is authenticated, check to see if the supplier is blocked in the user's country
    if user.is_authenticated:
        if user.country in supplier.blocked_countries.all():
            logging.debug(
                f"[SUPPLIER.API.GET_SUPPLIER] User is authenticated. User country: {user.country}. Supplier is blocked in user country."
            )
            return 403, ErrorSchema(
                success=False,
                message="Server understood the request, but is unwilling to process it",
            )

    # Change BaseResponseSchema to the schema you want to use for the response
    return 200, BaseResponseSchema(success=True, supplier=SupplierDetailedSchema.from_orm(supplier))  # type: ignore

    # Supplier.get_object_or_404(slug=supplier_slug)
    supplier = SupplierDetailedSchema.from_orm(supplier)



@supplier_router.get("/suppliers/{supplier_slug}/edit/profile")
def get_supplier_profile_admin(request: HttpRequest, supplier_slug: str):
    logging.debug("[SUPPLIER.API.GET_SUPPLIER_PROFILE_ADMIN] Called")

    # Get user
    user = request.user

    # Get supplier
    supplier = Supplier.objects.get(slug=supplier_slug)

    return 200, BaseResponseSchema(success=True, supplier=SupplierDetailedSchema.from_orm(supplier)) # type: ignore


@supplier_router.patch("/suppliers/{supplier_slug}/edit/company/seo")
def update_supplier_seo(request: HttpRequest, supplier_slug: str, data: SupplierUpdateSeoSchema):
    logging.debug('[SUPPLIER.API.UPDATE_SUPPLIER_SEO] Called')

    # Get supplier
    supplier = Supplier.objects.get(slug=supplier_slug)

    # Update supplier meta data
    supplier.meta_title = data.meta_title
    supplier.meta_description = data.meta_description
    supplier.meta_keywords = data.meta_keywords
    supplier.save()

    return 200, BaseResponseSchema(success=True, supplier=SupplierDetailedSchema.from_orm(supplier))