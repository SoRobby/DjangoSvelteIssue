import logging

from apps.accounts.api.router import accounts_router
from apps.accounts.schemas import LoginRequestSchema, LoginResponseSchema
from apps.core.schemas import ErrorSchema
from django.contrib.auth import authenticate, login
from ninja.errors import HttpError


# Login
@accounts_router.post("/auth/login", response={200: LoginResponseSchema, 401: ErrorSchema})
def login_view(request, data: LoginRequestSchema):
    """
    Handles user login and returns user information along with authentication status.
    """
    logging.info(f"[ACCOUNTS.API.LOGIN_VIEW] Login attempt for email: {data.email}")

    #  Authenticate the user, if user cannot be authenticated, return a 401 status code
    user = authenticate(email=data.email, password=data.password)
    if not user:
        logging.warning(f"Authentication failed for email: {data.email}")
        raise HttpError(status_code=401, message="Unable to login, the email and/or password is incorrect")

    # Log in the user and generate session key
    login(request, user)
    logging.debug(f"[ACCOUNTS.API.LOGIN_VIEW] User successfully logged in: {data.email}")

    # Prepare the response
    response_data = {
        "success": True,
        "message": "Login successful",
        "username": user.username,
        "email": user.email,
        "is_superuser": user.is_superuser,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "sessionid": request.session.session_key,
    }

    logging.debug("Login response data prepared for user: %s", user.email)
    return response_data
