import json
import logging
from typing import Optional

from apps.accounts.models import Account
from apps.core.schemas import BaseResponseSchema, ErrorSchema
from apps.feedback.models import FeedbackMessage
from apps.feedback.schemas import FeedbackMessageRequestSchema
from ninja import File, Form, NinjaAPI, Schema, UploadedFile
from ninja.files import UploadedFile
from ninja_jwt.authentication import JWTAuth
from PIL import Image

from .router import feedback_router


@feedback_router.post("/feedback", response={200: BaseResponseSchema, 403: ErrorSchema})
def submit_feedback(request, data: FeedbackMessageRequestSchema):
    """
    Registered or unregistered users can submit feedback
    """

    logging.debug(f"Feedback message: {data}")

    # If email value is present, attempt to get the user's profile
    if data.email:
        user = Account.objects.filter(email=data.email).first()
    else:
        user = None

    try:
        # Create feedback message
        FeedbackMessage.objects.create(
            user=user,
            name=data.name,
            email=data.email,
            page_url=data.page_url,
            content=data.content,
        )

        # Change BaseResponseSchema to the schema you want to use for the response
        return 200, BaseResponseSchema(
            success=True,
            message="Request was successful!",
        )
    except Exception as e:
        logging.error(f"Error submitting feedback: {e}")
        return 403, ErrorSchema(
            success=False,
            message="An error occurred while processing your request",
        )
