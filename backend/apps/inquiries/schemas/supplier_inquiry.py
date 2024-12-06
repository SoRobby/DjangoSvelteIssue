from typing import Optional

from ninja import Schema


# Request schemas
class SupplierInquiryCreateSchema(Schema):
    supplier_slug: str
    inquirer_username: Optional[str] = None
    inquirer_name: str
    inquirer_email: str
    inquirer_organization: str
    inquirer_position: Optional[str] = None
    inquirer_country_slug: str
    content: str