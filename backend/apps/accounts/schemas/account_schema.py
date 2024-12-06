from typing import List, Optional

from apps.accounts.models import Account, AccountInteraction, AccountSettings
from apps.core.schemas import (
    BaseResponseSchema,
    CountryBasicSchema,
    CountryDetailedSchema,
)
from apps.supplier.schemas import SupplierBasicSchema
from ninja import ModelSchema


# Model schemas
class AccountSettingsSchema(ModelSchema):
    class Meta:
        model = AccountSettings
        exclude = ["id", "account", "uuid", "date_created", "date_modified"]


class AccountInteractionSchema(ModelSchema):
    class Meta:
        model = AccountInteraction
        exclude = ["id", "account", "uuid", "date_created", "date_modified"]

# Account Public Schema
class AccountPublicSchema(ModelSchema):
    country: Optional[CountryBasicSchema] = None

    class Meta:
        model = Account
        fields = ["username", "email", "first_name", "last_name", "country"]


class AccountPublicResponseSchema(BaseResponseSchema):
    account: AccountPublicSchema


# Account Private Schemas
class AccountPrivateBasicSchema(ModelSchema):
    country: Optional[CountryDetailedSchema] = None
    managed_suppliers: List[SupplierBasicSchema] = []

    class Meta:
        model = Account
        fields = ["username", "email", "first_name", "last_name", "organization", "country", "profile_image_thumbnail", "is_staff", "is_admin", "is_superuser"]


class AccountPrivateDetailedSchema(ModelSchema):
    settings: Optional[AccountSettingsSchema] = None
    interactions: Optional[AccountInteractionSchema] = None
    country: Optional[CountryDetailedSchema] = None
    managed_suppliers: List[SupplierBasicSchema] = []

    class Meta:
        model = Account
        exclude = [
            "id",
            "email_verification_token",
            "password",
            "short_uuid",
            "date_last_logged_in",
            "is_deleted",
            "date_deleted",
            "email_verification_token_expiration_date",
        ]

class EditAccountResponseSchema(BaseResponseSchema):
    account: AccountPrivateDetailedSchema

# Public schemas
# Private schemas (user is logged in)
# Edit schema (user is editing info)