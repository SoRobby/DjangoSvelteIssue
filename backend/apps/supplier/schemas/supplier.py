from typing import List, Optional

from apps.core.schemas import BaseResponseSchema, CountryBasicSchema
from apps.supplier.models import Supplier, SupplierLocation
from ninja import ModelSchema, Schema

from .locations import SupplierLocationBasicSchema, SupplierLocationSchema
from .tags import SupplierTagSchema


# Schemas
class SupplierBasicSchema(ModelSchema):
    blocked_countries: List[CountryBasicSchema] = []
    locations: List[SupplierLocationBasicSchema] = []

    class Meta:
        model = Supplier
        fields = [
            "name",
            "legal_name",
            "slug",
            "acronym",
            "website",
            "tagline",
            "number_of_employees",
            "year_founded",
            "logo_thumbnail",
            "is_premium",
            "status",
            "blocked_countries",
        ]


class SupplierDetailedSchema(ModelSchema):
    blocked_countries: List[CountryBasicSchema] = []
    locations: List[SupplierLocationSchema] = []
    tags: List[SupplierTagSchema] = []

    class Meta:
        model = Supplier
        fields = "__all__"


class SupplierEditBasicInformationRequestSchema(Schema):
    acronym: Optional[str]
    tagline: Optional[str]
    description: Optional[str]
    website: Optional[str]


class SupplierUpdateSeoSchema(Schema):
    meta_title: Optional[str]
    meta_description: Optional[str]
    meta_keywords: Optional[str]


    # number_of_employees: Optional[str]
    # year_founded: Optional[int]
    # facebook_link: Optional[str]
    # twitter_link: Optional[str]
    # linkedin_link: Optional[str]
    # instagram_link: Optional[str]
    # youtube_link: Optional[str]
    # x_link: Optional[str]
