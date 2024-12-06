import logging

from apps.accounts.models import Account
from apps.accounts.schemas import (
    ResetPasswordConfirmRequestSchema,
    ResetPasswordRequestSchema,
)
from apps.core.schemas import BaseResponseSchema, ErrorSchema
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .router import accounts_router


@accounts_router.post("/auth/password-reset", response={200: BaseResponseSchema, 403: ErrorSchema})
def password_reset(request, data: ResetPasswordRequestSchema):
    logging.debug("[ACCOUNTS.API.PASSWORD_RESET] Called")

    logging.debug(settings.FRONTEND_ROOT_URL)

    # Check to see if the user exists, but don't reveal if the user exists
    try:
        user = Account.objects.get(email=data.email)
    except Account.DoesNotExist:
        # For security reasons, do not reveal whether the email exists
        return 200, BaseResponseSchema(
            success=True,
            message="If an account exists, a password reset email has been sent.",
            # Add the data here...
        )

    # Generate the token
    token = default_token_generator.make_token(user)
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

    # Construct the password reset url
    logging.debug(request.scheme)
    logging.debug(request.get_host())
    # reset_url = f"{request.scheme}://{request.get_host()}/reset-password?uidb64={uidb64}&token={token}"
    reset_url = f"{request.scheme}://{settings.FRONTEND_ROOT_URL}/reset-password/confirm?uidb64={uidb64}&token={token}"

    # Send email
    send_mail(
        "Password Reset Request",
        f"Click the link to reset your password: {reset_url}",
        "noreply@example.com",
        [user.email],
        fail_silently=False,
    )

    # Change BaseResponseSchema to the schema you want to use for the response
    return 200, BaseResponseSchema(success=True, message="Request was successful")


@accounts_router.post("/auth/password-reset/confirm", response={200: BaseResponseSchema, 400: ErrorSchema})
def password_reset_confirm(request, data: ResetPasswordConfirmRequestSchema):
    logging.debug("[ACCOUNTS.API.PASSWORD_RESET_CONFIRM] Called")

    try:
        uid = urlsafe_base64_decode(data.uidb64).decode()
        user = Account.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        logging.debug("[ACCOUNTS.API.PASSWORD_RESET_CONFIRM] UID or User does not exist")
        return 400, ErrorSchema(
            success=False,
            message="Password could not be reset, invalid token or user ID.",
        )

    if default_token_generator.check_token(user, data.token):
        try:
            validate_password(data.password1, user)
        except ValidationError as e:
            logging.debug(f"[ACCOUNTS.API.PASSWORD_RESET_CONFIRM] {e.messages}")
            return 400, ErrorSchema(
                success=False,
                message=" ".join(e.messages),
            )

        if data.password1 != data.password2:
            return 400, ErrorSchema(
                success=False,
                message="Passwords do not match.",
            )

        user.set_password(data.password1)
        user.save()

        return 200, BaseResponseSchema(
            success=True,
            message="Password has been reset successfully.",
        )
    else:
        return 400, ErrorSchema(
            success=False,
            message="Password could not be reset, invalid token.",
        )
