from typing import List, Optional

from apps.catalog.models import TaxonomyItemFile, TaxonomyItemFileVersion
from ninja import ModelSchema


class TaxonomyItemFileVersionSchema(ModelSchema):
    class Meta:
        model = TaxonomyItemFileVersion
        fields = "__all__"


class TaxonomyItemFileSchema(ModelSchema):
    latest_version: Optional[TaxonomyItemFileVersionSchema] = None
    
    class Meta:
        model = TaxonomyItemFile
        fields = "__all__"

