from decimal import Decimal
from typing import Any, Dict, List, Literal, Optional, Union

from apps.core.schemas import BaseResponseSchema
from apps.properties.models import Property
from django.db.models import Model
from ninja import ModelSchema, Schema
from pydantic import BaseModel, ConfigDict, Field, validator
from typing_extensions import Annotated

from .property_type_schemas import (
    FloatPropertyBasicSchema,
    IntegerPropertyBasicSchema,
    StringPropertyBasicSchema,
)


class PropertyTypeDetailsSchema(Schema):
    default_value: Optional[Union[str, float, int]] = None  # Accept multiple types for default_value
    is_min_limit_enabled: Optional[bool] = None
    is_max_limit_enabled: Optional[bool] = None
    min_limit_value: Optional[float] = None
    max_limit_value: Optional[float] = None
    step_size: Optional[int] = None
    units_prefix: Optional[str] = None
    units_suffix: Optional[str] = None


# Schemas
class PropertyBasicSchema(ModelSchema):
    details: Optional[PropertyTypeDetailsSchema] = None  # Add this field explicitly as a schema-level attribute.

    class Meta:
        model = Property
        fields = ["name", "slug", "key", "property_type", "is_builtin", "description"]

    @staticmethod
    def resolve_details(obj: Property):
        if obj.property_type == Property.PropertyTypeChoices.INTEGER:
            integer_property = getattr(obj, 'integer_property', None)
            if integer_property:
                return {
                    "default_value": integer_property.default_value,
                    "is_min_limit_enabled": integer_property.is_min_limit_enabled,
                    "is_max_limit_enabled": integer_property.is_max_limit_enabled,
                    "min_limit_value": integer_property.min_limit_value,
                    "max_limit_value": integer_property.max_limit_value,
                    "units_prefix": integer_property.units_prefix,
                    "units_suffix": integer_property.units_suffix
                }
        elif obj.property_type == Property.PropertyTypeChoices.FLOAT:
            float_property = getattr(obj, 'float_property', None)
            if float_property:
                return {
                    "default_value": float_property.default_value,
                    "step_size": float_property.step_size,
                    "is_min_limit_enabled": float_property.is_min_limit_enabled,
                    "is_max_limit_enabled": float_property.is_max_limit_enabled,
                    "min_limit_value": float_property.min_limit_value,
                    "max_limit_value": float_property.max_limit_value,
                    "units_prefix": float_property.units_prefix,
                    "units_suffix": float_property.units_suffix
                }
        elif obj.property_type == Property.PropertyTypeChoices.STRING:
            string_property = getattr(obj, 'string_property', None)
            if string_property:
                return {
                    "default_value": string_property.default_value,
                }
        return None

