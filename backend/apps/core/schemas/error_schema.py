from typing import List, Optional, Union

from ninja import Schema


class Error400Schema(Schema):
    field: str
    message: str

class Error500Schema(Schema):
    code: str
    message: str

class ErrorSchema(Schema):
    success: bool=False
    message: Optional[str] = None
    errors: Optional[List[Union[Error400Schema, Error500Schema]]] = None
