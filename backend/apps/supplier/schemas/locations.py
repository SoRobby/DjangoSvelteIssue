from apps.core.schemas import CountryBasicSchema
from apps.supplier.models import SupplierLocation
from ninja import ModelSchema


# Schemas
class SupplierLocationBasicSchema(ModelSchema):
    country: CountryBasicSchema

    class Meta:
        model = SupplierLocation
        fields = ["city", "subnational_region", "country", "name", "is_headquarters"]


class SupplierLocationSchema(ModelSchema):
    country: CountryBasicSchema

    class Meta:
        model = SupplierLocation
        fields = ["address1", "address2", "city", "postal_code", "subnational_region", "country", "name", "description", "website", "is_headquarters"]
