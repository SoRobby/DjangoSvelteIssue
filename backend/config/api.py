"""
Project API route app configuration.
"""

import json
import logging

from apps.accounts.api.router import accounts_router
from apps.catalog.api.router import catalog_router
from apps.core.api.router import core_router
from apps.feedback.api.router import feedback_router
from apps.inquiries.api.router import inquiries_router
from apps.supplier.api.router import supplier_router
from apps.tools.api.router import tools_router
from django.http import HttpResponse
from ninja.errors import AuthenticationError, HttpError, ValidationError
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

# Define Django Ninja API
api = NinjaExtraAPI(version="1.0.0", csrf=False, title="DjangoNextAPI")
api.register_controllers(NinjaJWTDefaultController)


# Custom error handler for Ninja API
@api.exception_handler(ValidationError)
def validation_errors(request, exc: ValidationError):
    logging.error(f"Validation error: {exc.errors}")

    # Extract all error messages by concatenating them
    error_messages = "; ".join([error.get("msg", "Unknown validation error") for error in exc.errors])
    error_messages = error_messages.capitalize()

    # Structure the response in a clean and consistent way
    response_data = {
        "success": False,
        "message": error_messages,
        "detail": exc.errors,
    }

    return HttpResponse(
        json.dumps(response_data, ensure_ascii=False, indent=2),
        status=400,
        content_type="application/json",
    )



# Create Ninja API routes
# Add routes to the main API instance, root is ./api/
api.add_router("/v1/", accounts_router, tags=["Accounts"])
api.add_router("/v1/", core_router, tags=["Core"])
api.add_router("/v1/", catalog_router, tags=["Catalog"])
api.add_router("/v1/", tools_router, tags=["Tools"])
api.add_router("/v1/", supplier_router, tags=["Supplier"])
api.add_router("/v1/", feedback_router, tags=["Feedback"])
api.add_router("/v1/inquiries/", inquiries_router, tags=["Inquiries"])
