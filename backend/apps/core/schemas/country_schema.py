from apps.core.models import Country
from ninja import ModelSchema


# Schemas
class CountryBasicSchema(ModelSchema):
    class Meta:
        model = Country
        fields = ["name", "slug", "iso_code_alpha2", "iso_code_alpha3"]


class CountryDetailedSchema(ModelSchema):
    class Meta:
        model = Country
        fields = ["name", "slug", "iso_code_numeric", "iso_code_alpha2", "iso_code_alpha3", "phone_code", "flag"]
