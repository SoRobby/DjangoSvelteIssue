from apps.accounts.models import Account
from apps.core.schemas import BaseResponseSchema
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from ninja import ModelSchema, Schema
from pydantic import BaseModel, EmailStr, HttpUrl, SecretStr, constr, validator

# REF: https://chatgpt.com/c/e1580dec-b65d-413a-84bc-09fb32d8d005


# Register
# class RegisterSchema(ModelSchema):
#     class Meta:
#         model = Account
#         fields = ['username', 'email', '']


class RegisterRequestSchema(BaseModel):
    # TODO - After testing is complete add SecretStr to password1 and password2
    username: constr(min_length=4, max_length=16) # type: ignore
    email: EmailStr
    password1: str
    password2: str
    first_name: constr(max_length=120) # type: ignore
    last_name: constr(max_length=120) # type: ignore

    # last_name: constr(max_length=120)
    # country: str
    # organization: constr(max_length=255) = None

    # @validator("username")
    # def validate_unique_username(cls, value):
    #     print('checking validtion')
    #     if Account.objects.filter(username__iexact=value).exists():
    #         raise ValidationError("Username already exists")
    #     return value

    # if UserModel.objects.filter(username__iexact=value).exists():
    #     exception = APIException("Username already exists")
    #     exception.status_code = status.HTTP_400_BAD_REQUEST
    #     raise exception
    # return value

    # username: str
    # password1: str
    # password2: str
    # first_name: str
    # last_name: str
    # country: str
    # organization: str = None


class RegisterResponseSchema(BaseResponseSchema):
    username: str
    email: str
    is_superuser: bool
    first_name: str
    last_name: str
    sessionid: str
