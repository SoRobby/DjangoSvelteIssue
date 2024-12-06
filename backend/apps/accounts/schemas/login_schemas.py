from apps.core.schemas import BaseResponseSchema
from ninja import Schema


class LoginRequestSchema(Schema):
    email: str
    password: str


class LoginResponseSchema(BaseResponseSchema):
    username: str
    email: str
    is_superuser: bool
    first_name: str
    last_name: str
    sessionid: str