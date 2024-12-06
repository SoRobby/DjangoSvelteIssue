import logging
import re
from typing import Tuple, Union

from apps.accounts.api.router import accounts_router
from apps.accounts.models import Account
from apps.accounts.reserved_usernames import reserved_names
from apps.accounts.schemas import RegisterRequestSchema, RegisterResponseSchema
from apps.core.schemas import BaseResponseSchema, Error400Schema, ErrorSchema
from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from pydantic import EmailStr


# Functions
def validate_username(username: str) -> Tuple[bool, Union[str, None]]:
    is_valid: bool = True
    message: Union[str, None] = None

    # Check to see if email is already being used:
    if Account.objects.filter(username__iexact=username).exists():
        logging.debug(f"Status: Username is unavailable")
        is_valid = False
        message = "This username is unavailable"

    if len(username) < 4 or len(username) > 16:
        logging.debug(f"Status: Username is invalid. Username must be between 4 and 16 characters")
        is_valid = False
        message = "Username must be between 4 and 16 characters"

    if re.match(r"^[a-zA-Z0-9_]*$", username) == None:
        logging.debug(f"Status: Username is invalid. Username must only contain letters, numbers, and underscores")
        is_valid = False
        message = "Username must only contain letters, numbers, and underscores"

    if username in reserved_names:
        logging.debug(f"Status: Username is invalid. Username is reserved")
        is_valid = False
        message = "This username is unavailable"

    return is_valid, message


def validate_email(email: EmailStr) -> Tuple[bool, Union[str, None]]:
    is_valid: bool = True
    message: Union[str, None] = None

    if Account.objects.filter(email__iexact=email).exists():
        logging.debug(f"Status: Email is unavailable")
        is_valid = False
        message = "This email is unavailable"

    return is_valid, message


def validate_password_wrapper(password1: str, password2: str) -> Tuple[bool, Union[str, None]]:
    # First, check if the passwords match
    if password1 != password2:
        return False, "Passwords do not match"

    # Check if password length is within valid bounds
    if len(password1) > 255:
        return False, "Passwords cannot be longer than 255 characters"

    if len(password1) < 6:
        return False, "Password must be at least 6 characters long"

    try:
        validate_password(password1)
    except ValidationError as e:
        return False, " ".join(e.messages)

    # If no errors, return success
    return True, None


# API Endpoints
@accounts_router.get("/auth/register/validate-email", response={200: BaseResponseSchema, 409: ErrorSchema})
def validate_email_view(request, email: EmailStr):
    logging.debug("[ACCOUNTS.API.VALIDATE_EMAIL_VIEW] Called")
    logging.debug(f"Email: {email}")

    is_valid, message = validate_email(email)

    if not is_valid:
        return 409, ErrorSchema(
            success=False,
            message=message,
        )
    else:
        return 200, BaseResponseSchema(success=True, message="Email is available")


@accounts_router.get("/auth/register/validate-username", response={200: BaseResponseSchema, 409: ErrorSchema})
def validate_username_view(request, username: str):
    logging.debug("[ACCOUNTS.API.VALIDATE_USERNAME_VIEW] Called")
    logging.debug(f"\tUsername: {username}")

    is_valid, message = validate_username(username)

    if not is_valid:
        return 409, ErrorSchema(
            success=False,
            message=message,
        )
    else:
        return 200, BaseResponseSchema(success=True, message="Username is available")


@accounts_router.post("/auth/register", response={200: RegisterResponseSchema, 400: ErrorSchema, 403: ErrorSchema, 422: ErrorSchema, 500: ErrorSchema})
def register_view(request, data: RegisterRequestSchema):
    logging.debug("[ACCOUNTS.API.REGISTER_VIEW] Called")

    user = request.user

    # Verify that the user is not already authenticated
    if user.is_authenticated:
        return 400, ErrorSchema(
            success=False,
            message="User is already authenticated and logged in",
        )

    # Perform username and email validations
    validation_errors = []
    error_message = None

    is_email_valid, email_message = validate_email(data.email)
    if not is_email_valid:
        error_message = "Error with email address."
        validation_errors.append(Error400Schema(field="email", message=email_message))

    is_username_valid, username_message = validate_username(data.username)
    if not is_username_valid:
        error_message = f"{error_message} Error with username."
        validation_errors.append(Error400Schema(field="username", message=username_message))

    if validation_errors:
        logging.debug(f"[ACCOUNTS.API.REGISTER_VIEW] Validation errors: {validation_errors}")
        return 400, ErrorSchema(success=False, message=error_message, errors=validation_errors)

    # Validate passwords to ensure they match
    is_password_valid, password_message = validate_password_wrapper(data.password1, data.password2)
    if not is_password_valid:
        return 422, ErrorSchema(
            success=False,
            message=password_message,
            errors=[Error400Schema(field="password1", message=password_message)],
        )

    # Try to create the account
    try:
        logging.debug("[ACCOUNTS.API.REGISTER_VIEW] Creating account")
        account = Account.objects.create(
            username=data.username,
            email=data.email,
            first_name=data.first_name,
            last_name=data.last_name,
        )

        # Set the password and hash it using set_password
        account.set_password(data.password1)
        account.save()

        logging.debug("[ACCOUNTS.API.REGISTER_VIEW] Account created")

        user = authenticate(request, email=data.email, password=data.password1)

        logging.debug("[ACCOUNTS.API.REGISTER_VIEW] User authenticated")
        logging.debug(f"[ACCOUNTS.API.REGISTER_VIEW] User: {user}")

        if user is not None:
            login(request, user)
            logging.debug("[ACCOUNTS.API.REGISTER_VIEW] User logged in")

            # Change BaseResponseSchema to the schema you want to use for the response
            return 200, RegisterResponseSchema(
                success=True,
                message="Account successfully created and user logged in",
                username=user.username,
                email=user.email,
                is_superuser=user.is_superuser,
                first_name=user.first_name,
                last_name=user.last_name,
                sessionid=request.session.session_key,
            )

        else:
            logging.error("[ACCOUNTS.API.REGISTER_VIEW] Error: User is None")
            return 400, ErrorSchema(
                success=False,
                message="Account was successfully created, but an error occurred while logging in",
            )

    except Exception as e:
        logging.error(f"[ACCOUNTS.API.REGISTER_VIEW] Error: {e}")
        # HTTP Error 500: Unexpected error occurred on the server side
        return 500, ErrorSchema(
            success=False,
            message="Unexpected error occurred while creating the account",
        )
