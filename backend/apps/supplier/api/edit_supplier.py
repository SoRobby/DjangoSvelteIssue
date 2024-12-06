import logging
from typing import Any, List

from apps.core.schemas import BaseResponseSchema, ErrorSchema
from apps.supplier.models import Permission, Role, Supplier, UserRole
from apps.supplier.schemas import (
    SupplierBasicSchema,
    SupplierDetailedSchema,
    SupplierEditBasicInformationRequestSchema,
)
from apps.supplier.utils import is_user_linked_to_supplier
from django.http import HttpRequest
from ninja_jwt.authentication import JWTAuth

from .router import supplier_router


@supplier_router.get(
    "/suppliers/{supplier_slug}/admin", auth=JWTAuth(), response={200: BaseResponseSchema, 403: ErrorSchema}
)
def supplier_admin_get(request: HttpRequest, supplier_slug: str):
    logging.debug("[SUPPLIER.API.SUPPLIER_ADMIN] Called")

    # Get user
    user = request.user

    # Get the supplierE
    supplier = Supplier.objects.get(slug=supplier_slug)

    if user.is_superuser or user.is_admin:
        supplier_data = SupplierDetailedSchema.from_orm(supplier)
        return 200, BaseResponseSchema(success=True, supplier=supplier_data)
    if is_user_linked_to_supplier(user, supplier):
        supplier_data = SupplierDetailedSchema.from_orm(supplier)
        return 200, BaseResponseSchema(success=True, supplier=supplier_data)
    else:
        return 403, ErrorSchema(
            success=False,
            message="User is not authenticated",
        )


@supplier_router.patch(
    "/suppliers/{supplier_slug}/admin/basic-information",
    auth=JWTAuth(),
    response={200: BaseResponseSchema, 403: ErrorSchema},
)
def supplier_admin_patch(request: HttpRequest, supplier_slug: str, data: SupplierEditBasicInformationRequestSchema):
    logging.debug("[SUPPLIER.API.SUPPLIER_ADMIN] Called")

    # Get user
    user = request.user

    # Get the supplier
    supplier = Supplier.objects.get(slug=supplier_slug)

    if user.is_superuser or user.is_admin:
        logging.debug(data)

        # Update the supplier basic information
        if type(data.acronym) == str:
            supplier.acronym = data.acronym.strip()
        else:
            supplier.acronym = None

        if type(data.tagline) == str:
            supplier.tagline = data.tagline.strip()
        else:
            supplier.tagline = None
        
        if type(data.description) == str:
            supplier.description = data.description.strip()
        else:
            supplier.description = None

        if type(data.website) == str:
            supplier.website = data.website.strip()
        else:
            supplier.website = None
        
        supplier.save()

        supplier_data = SupplierDetailedSchema.from_orm(supplier)

        # Perform the update to the supplier
        

        return 200, BaseResponseSchema(success=True, supplier=supplier_data)
    if is_user_linked_to_supplier(user, supplier):
        supplier_data = SupplierDetailedSchema.from_orm(supplier)
        return 200, BaseResponseSchema(success=True, supplier=supplier_data)
    else:
        return 403, ErrorSchema(
            success=False,
            message="User is not authenticated",
        )
