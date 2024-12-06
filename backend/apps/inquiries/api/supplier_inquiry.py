import logging

from apps.accounts.models import Account
from apps.core.models import Country
from apps.core.schemas import BaseResponseSchema, ErrorSchema
from apps.inquiries.models import SupplierInquiry
from apps.inquiries.schemas import SupplierInquiryCreateSchema
from apps.supplier.models import Supplier

from .router import inquiries_router

# Base URL for inquiries_router is: /api/v1/inquiries/


@inquiries_router.post("/supplier", response={200: BaseResponseSchema, 403: ErrorSchema})
def create_supplier_inquiry(request, data: SupplierInquiryCreateSchema):
    logging.debug("[INQUIRIES.API.CREATE_SUPPLIER_INQUIRY] Called")
    logging.debug(f"Data: {data}")

    # TODO - If user is not authenticated and email exists, try to get user by email
    if request.user.is_authenticated:
        inquirer_user = request.user
    else:
        try:
            inquirer_user = Account.objects.get(email=data.inquirer_email)
        except Account.DoesNotExist:
            inquirer_user = None

    try:
        # Get supplier
        supplier = Supplier.objects.get(slug=data.supplier_slug)

        # Get country
        country = Country.objects.get(slug=data.inquirer_country_slug)

        SupplierInquiry.objects.create(
            supplier=supplier,
            inquirer=inquirer_user,
            name=data.inquirer_name,
            email=data.inquirer_email,
            organization=data.inquirer_organization,
            position=data.inquirer_position,
            country=country,
            content=data.content,
        )

        # Change BaseResponseSchema to the schema you want to use for the response
        return 200, BaseResponseSchema(success=True, message=f"Message successfully sent to {supplier.name}")
    except Exception as e:
        logging.error(f"[INQUIRIES.API.CREATE_SUPPLIER_INQUIRY] Error: {e}")
        return 403, ErrorSchema(success=False, message="Unable to send message")
