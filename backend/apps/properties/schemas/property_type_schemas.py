from typing import List

from apps.core.schemas import BaseResponseSchema
from apps.properties.models import FloatProperty, IntegerProperty, StringProperty
from ninja import ModelSchema


# Schemas
class IntegerPropertyBasicSchema(ModelSchema):
    class Meta:
        model = IntegerProperty
        fields = "__all__"


class FloatPropertyBasicSchema(ModelSchema):
    class Meta:
        model = FloatProperty
        fields = "__all__"


class StringPropertyBasicSchema(ModelSchema):
    class Meta:
        model = StringProperty
        fields = "__all__"