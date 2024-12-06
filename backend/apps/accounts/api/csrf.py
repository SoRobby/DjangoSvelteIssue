# import logging

# from apps.accounts.api.router import accounts_router
# from apps.core.schemas import BaseResponseSchema
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie


# @accounts_router.post("/auth/csrf-token")
# @ensure_csrf_cookie
# @csrf_exempt
# def get_csrf_token(request):
#     logging.debug("[ACCOUNTS.API.CSRF] get_csrf_token()")

#     # Log the request method and the request headers to check for CORS issues
#     logging.debug(f"\tRequest Method: {request.method}")
#     logging.debug(f"\tRequest Headers: {dict(request.headers)}")
    
#     # Log the CSRF cookie in the response
#     csrf_cookie = request.COOKIES.get("csrftoken")
#     logging.debug(f"\tCSRF Cookie: {csrf_cookie}")

#     return HttpResponse()


# @accounts_router.post("/auth/csrf-token/validate", response={200: BaseResponseSchema})
# def validate_csrf_token(request):
#     logging.debug("[ACCOUNTS.API.CSRF] validate_csrf_token()")

#     # Log request headers for CORS debug information
#     logging.debug(f"\tRequest Headers: {dict(request.headers)}")

#     csrf_token = request.META.get("HTTP_X_CSRFTOKEN")
#     logging.debug(f"\tCSRF Token (Header): {csrf_token}")

#     # Log CSRF cookie to compare against the CSRF token in the request
#     csrf_cookie = request.COOKIES.get("csrftoken")
#     logging.debug(f"\tCSRF Cookie: {csrf_cookie}")

#     # Check if the CSRF token matches the cookie and log the result
#     if csrf_token == csrf_cookie:
#         logging.debug("\tCSRF token is valid and matches the CSRF cookie.")
#     else:
#         logging.debug("\tCSRF token is invalid or does not match the CSRF cookie.")
    
    
#     return 200, BaseResponseSchema(
#             success=True,
#             message="CSRF token is valid"
#         )


