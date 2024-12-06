import logging
import uuid
from uuid import uuid4

from apps.accounts.models import Account
from apps.accounts.schemas import EmailVerificationRequestSchema
from apps.core.schemas import BaseResponseSchema, ErrorSchema
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from ninja_jwt.authentication import JWTAuth

from .router import accounts_router


@accounts_router.put(
    "/auth/email-verification/send", auth=JWTAuth(), response={200: BaseResponseSchema, 403: ErrorSchema}
)
def send_email_verification(request):
    # When a new email verification token is requested, a new email verification token and expiration date of that token
    # will be generated.

    logging.debug("[ACCOUNTS.API.SEND_EMAIL_VERIFICATION] Called")

    # Get the current user
    user = request.user

    # Generate a new email verification UUID token
    user.email_verification_token = uuid4()
    user.email_verification_token_expiration_date = timezone.now() + timezone.timedelta(days=7)
    user.save()

    uidb64 = urlsafe_base64_encode(force_bytes(user.email_verification_token))
    decode = urlsafe_base64_decode(uidb64)

    verify_email_url = f"{request.scheme}://{settings.FRONTEND_ROOT_URL}/email-verification/confirm?token={uidb64}"



    logging.debug(user.email_verification_token)
    logging.debug(uidb64)
    logging.debug(decode)

    send_mail(
        subject="[COMPANY NAME] Email Verification",
        message=f"Hello, please verify your email by clicking the following link: \n {verify_email_url}",
        from_email=settings.EMAIL_ADDRESSES.NO_REPLY,
        recipient_list=[str(user.email)],
        fail_silently=False,
    )

    # Change BaseResponseSchema to the schema you want to use for the response
    return 200, BaseResponseSchema(
        success=True,
        message="Email has been sent to your email address. Please verify your email.",
    )


@accounts_router.post("/auth/email-verification/confirm", response={200: BaseResponseSchema, 403: ErrorSchema})
def verify_email(request, payload: EmailVerificationRequestSchema):
    logging.debug("[ACCOUNTS.API.VERIFY_EMAIL] Email verification process started.")

    logging.debug(f"Payload received: {payload}")

    # Decode the token from base64 format
    decoded_token_bytes = urlsafe_base64_decode(payload.token)

    # Convert the byte string to a regular string
    decoded_token_str = decoded_token_bytes.decode("utf-8")

    logging.debug(f"Decoded token (bytes): {decoded_token_bytes}")
    logging.debug(f"Decoded token (string): {decoded_token_str}")

    try:
        # Parse the string as a UUID
        email_verification_uuid = uuid.UUID(decoded_token_str)

        # Look up the user based on the decoded UUID token
        user = Account.objects.get(email_verification_token=email_verification_uuid)
        logging.debug(f"Verified token UUID: {email_verification_uuid}")

        # Check to see if the email verification token has expired
        if user.email_verification_token_expiration_date and user.email_verification_token_expiration_date < timezone.now():
            logging.error(f"Email verification token has expired: '{decoded_token_str}'")
            return 403, ErrorSchema(
                success=False,
                message="The email verification token is invalid or has expired.",
            )

        user.is_email_verified = True
        user.save()
        return 200, BaseResponseSchema(success=True)
    except ValueError:
        logging.error(f"Invalid UUID: '{decoded_token_str}'")
        return 403, ErrorSchema(
            success=False,
            message="The email verification token is invalid or has expired.",
        )

    except Account.DoesNotExist:
        logging.error(f"Account with token '{email_verification_uuid}' not found")
        return ErrorSchema(message="Invalid email verification token")
