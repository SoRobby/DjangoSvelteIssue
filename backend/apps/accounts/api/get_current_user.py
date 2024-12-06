import logging

from apps.accounts.schemas import AccountPrivateBasicSchema
from apps.core.schemas import BaseResponseSchema, ErrorSchema
from apps.supplier.models import Supplier, SupplierRole, UserRole
from ninja_jwt.authentication import JWTAuth

from .router import accounts_router


@accounts_router.get("/auth/get-current-user", auth=JWTAuth(), response={200: BaseResponseSchema, 403: ErrorSchema})
def get_current_user(request):
    logging.debug("[ACCOUNTS.API.GET_CURRENT_USER] Called")
    user = request.user
    if user.is_authenticated:

        # See if the user is admin of an suppliers
        user_roles = UserRole.objects.filter(user=user)

        # Use the related role to get the supplier linked to each role
        suppliers = Supplier.objects.filter(supplier_roles__user_roles__in=user_roles).distinct()

        logging.debug(f"\tUser Roles: {user_roles}")
        logging.debug(f"\tSuppliers: {suppliers}")

        user.managed_suppliers = suppliers
        account = AccountPrivateBasicSchema.from_orm(user)

        return 200, BaseResponseSchema(
            success=True,
            message="Request was successful",
            account=account,  # type: ignore
        )
    else:
        # HTTP Error 403: Server understood the request, but is unwilling to process it
        logging.debug("[ACCOUNTS.API.GET_CURRENT_USER] User is not authenticated")
        return 403, ErrorSchema(
            success=False,
            message="User is not authenticated or logged in",
        )

