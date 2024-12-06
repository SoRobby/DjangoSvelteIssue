from typing import List

from apps.core.models import Country
from apps.core.schemas import BaseResponseSchema, CountryBasicSchema

from .router import core_router


@core_router.get("/countries")
def get_countries(request):
    countries = Country.objects.all()
    country_data = [CountryBasicSchema.from_orm(country) for country in countries]

    return 200, BaseResponseSchema(
            success=True,
            message="Request was successful",
            countries=country_data # type: ignore
        )

