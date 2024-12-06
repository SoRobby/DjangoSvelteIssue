from typing import Optional

from ninja import Schema


# Request schemas
class ItemInquiryCreateSchema(Schema):
    item_slug: str
    inquirer_username: Optional[str] = None
    inquirer_name: str
    inquirer_email: str
    inquirer_organization: str
    inquirer_position: Optional[str] = None
    inquirer_country_slug: str
    content: str

    # Request information
    request_datasheet: Optional[bool] = False
    request_icd: Optional[bool] = False
    request_options_sheet: Optional[bool] = False
    request_user_manual: Optional[bool] = False
    request_cad_model: Optional[bool] = False
    request_quotation: Optional[bool] = False
    request_lead_time: Optional[bool] = False
    request_heritage: Optional[bool] = False
