from typing import Optional

from ninja import Schema


class UnitsSchema(Schema):
    prefix: Optional[str] = None
    suffix: Optional[str] = None


class OutputValueSchema(Schema):
    name: str
    value: float
    units: Optional[UnitsSchema] = None
    tooltip: Optional[str] = None
