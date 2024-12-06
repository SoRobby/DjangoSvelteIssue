from apps.supplier.models import SupplierTag
from ninja import ModelSchema


# Schemas
class SupplierTagSchema(ModelSchema):
    class Meta:
        model = SupplierTag
        fields = ["name", "slug", "description"]
