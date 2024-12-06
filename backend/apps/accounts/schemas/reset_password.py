from apps.accounts.models import Account
from apps.core.schemas import BaseResponseSchema
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from ninja import ModelSchema, Schema
from pydantic import BaseModel, EmailStr, HttpUrl, SecretStr, constr, validator


class ResetPasswordRequestSchema(Schema):
    email: EmailStr


class ResetPasswordConfirmRequestSchema(Schema):
    uidb64: str
    token: str
    password1: str
    password2: str