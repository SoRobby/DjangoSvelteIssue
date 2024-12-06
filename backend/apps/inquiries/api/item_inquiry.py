import logging

from apps.accounts.models import Account
from apps.core.models import Country
from apps.core.schemas import BaseResponseSchema, ErrorSchema
from apps.inquiries.models import ItemInquiry, SupplierInquiry
from apps.inquiries.schemas import ItemInquiryCreateSchema
from apps.supplier.models import Supplier

from .router import inquiries_router


@inquiries_router.post("/item", response={200: BaseResponseSchema, 403: ErrorSchema})
def create_item_inquiry(request, data: ItemInquiryCreateSchema):
    logging.debug("[INQUIRIES.API.CREATE_ITEM_INQUIRY] Called")
    logging.debug(f"Data: {data}")

    # See if user is logged in
    logging.debug(f"request.user = {request.user}")

    try:
        # Create inquiry:
        ItemInquiry.objects.create(
            name=data.inquirer_name,
            email=data.inquirer_email,
            organization=data.inquirer_organization,
            country=Country.objects.get(slug=data.inquirer_country_slug),
            content=data.content,

            # request_datasheet=data.request_datasheet,
            # request_icd=data.request_icd,
            # request_options_sheet=data.request_options_sheet,
            # request_user_manual=data.request_user_manual,
            # request_cad_model=data.request_cad_model,
            # request_quotation=data.request_quotation,
            # request_lead_time=data.request_lead_time,
            # request_heritage=data.request_heritage,
        )

        # Change BaseResponseSchema to the schema you want to use for the response
        return 200, BaseResponseSchema(success=True, message="Request was successful")
    except Exception as e:
        return 403, ErrorSchema(
            success=False,
            message="Server understood the request, but is unwilling to process it",
        )
