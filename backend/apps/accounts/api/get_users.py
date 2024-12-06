import logging

from apps.accounts.models import Account
from apps.accounts.schemas import (
    AccountPrivateBasicSchema,
    AccountPrivateDetailedSchema,
    AccountPublicResponseSchema,
    AccountPublicSchema,
)
from apps.core.schemas import BaseResponseSchema, ErrorSchema
from apps.supplier.models import Supplier, SupplierRole, UserRole
from ninja_jwt.authentication import JWTAuth

from .router import accounts_router


@accounts_router.get("/auth/get-users", response={200: BaseResponseSchema, 403: ErrorSchema})
def get_users(request):
    logging.debug("[ACCOUNTS.API.GET_USERS] Called")

    users = Account.objects.all()
    profiles = [
        AccountPublicSchema(
            username=user.username,  # type: ignore
            email=user.email,  # type: ignore
            first_name=user.first_name,  # type: ignore
            last_name=user.last_name,  # type: ignore
            is_superuser=user.is_superuser,  # type: ignore
            country=user.country,  # type: ignore
        )
        for user in users
    ]

    # Change BaseResponseSchema to the schema you want to use for the response
    return 200, BaseResponseSchema(
        success=True,
        message="Request was successful",
        profiles=profiles,  # type: ignore
    )


@accounts_router.get("/auth/get-users/{username}", response={200: BaseResponseSchema, 403: ErrorSchema})
def get_user(request, username: str):
    logging.debug("[ACCOUNTS.API.GET_USER] get_user")

    profile = Account.objects.get(username=username)
    profile = AccountPublicSchema.from_orm(profile)

    # Change BaseResponseSchema to the schema you want to use for the response
    return 200, BaseResponseSchema(
        success=True,
        message="Request was successful",
        profile=profile,  # type: ignore
    )