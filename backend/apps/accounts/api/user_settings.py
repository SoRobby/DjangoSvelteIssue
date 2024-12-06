import hashlib
import json
import logging
from typing import Optional

from apps.accounts.schemas import (
    AccountPrivateDetailedSchema,
    DeleteUserRequestSchema,
    EditAccountResponseSchema,
    UpdateUserGeneralSchema,
    UpdateUserNotificationsSchema,
    UpdateUserProfileImageSchema,
    UserEditSchema,
)
from apps.core.models import Country
from apps.core.schemas import BaseResponseSchema, ErrorSchema
from apps.feedback.models import SupportMessage
from apps.feedback.schemas import SupportMessageRequestSchema
from django.contrib.auth import authenticate
from ninja import File, Form, NinjaAPI, Schema, UploadedFile
from ninja.files import UploadedFile
from ninja_jwt.authentication import JWTAuth
from PIL import Image

from .router import accounts_router


@accounts_router.get(
    "/auth/edit/user-general", auth=JWTAuth(), response={200: EditAccountResponseSchema, 403: ErrorSchema}
)
def edit_user_general_get(request):
    logging.debug("[ACCOUNTS.API.EDIT_USER_GENERAL] Called")

    user = request.user

    if user.is_authenticated:
        account_data = AccountPrivateDetailedSchema.from_orm(user)
        return 200, EditAccountResponseSchema(success=True, message="Request was successful", account=account_data)
    else:
        logging.debug("[ACCOUNTS.API.EDIT_USER_GENERAL] User is not authenticated")
        # HTTP Error 403: Server understood the request, but is unwilling to process it
        return 403, ErrorSchema(
            success=False,
            message="Unable to authenticate user",
        )


@accounts_router.post(
    "/auth/edit/user-general", auth=JWTAuth(), response={200: EditAccountResponseSchema, 403: ErrorSchema}
)
def edit_user_general_post(request, data: Form[UpdateUserGeneralSchema], profile_image: Optional[UploadedFile] = File(None)):
    logging.debug("[ACCOUNTS.API.EDIT_USER_GENERAL] Called")
    user = request.user
    if user.is_authenticated:
        logging.debug(f"\tData: {data}")

        user.first_name = data.first_name
        user.last_name = data.last_name
        user.bio = data.bio
        user.organization = data.organization
        user.position = data.position

        # See if the country changed if so, update the country
        if user.country.slug != data.country_slug:
            country = Country.objects.get(slug=data.country_slug)
            user.country = country

        # # Profile image
        # if profile_image:
        #     cropped_image_details = json.loads(request.POST["cropped_image_details"])
        #     image_crop_x: int = int(cropped_image_details["x"])
        #     image_crop_y: int = int(cropped_image_details["y"])
        #     image_crop_width: int = int(cropped_image_details["width"])
        #     image_crop_height: int = int(cropped_image_details["height"])

        #     user.add_profile_image_with_cropping(
        #         profile_image, image_crop_x, image_crop_y, image_crop_width, image_crop_height
        #     )

        user.save()

        account_data = AccountPrivateDetailedSchema.from_orm(user)
        return 200, EditAccountResponseSchema(
            success=True, message="Settings successfully updated", account=account_data
        )
    else:
        logging.debug("[ACCOUNTS.API.EDIT_USER_GENERAL] User is not authenticated")
        return 403, ErrorSchema(
            success=False,
            message="Unable to authenticate user",
        )


@accounts_router.post(
    "/auth/edit/profile-image", auth=JWTAuth(), response={200: EditAccountResponseSchema, 403: ErrorSchema}
)
def edit_update_profile_image(
    request, data: Form[UpdateUserProfileImageSchema], profile_image: Optional[UploadedFile] = File(None)
):
    logging.debug("[ACCOUNTS.API.EDIT_UPDATE_PROFILE_IMAGE] Called")
    user = request.user
    if user.is_authenticated:
        logging.debug(f"\tData: {data}")
        logging.debug(f"\tProfile Image: {profile_image}")

        user.last_name = data.last_name.strip()

        # Check to see if a profile image was uploaded


            # # Parse out the image details
            # cropped_image_details = json.loads(request.POST["cropped_image_details"])
            # profile_image_uploaded_hash = hashlib.md5(profile_image.read()).hexdigest()

            # logging.critical(f"cropped_image_details: {cropped_image_details}")
            # logging.critical(f"uploaded_hash: {profile_image_uploaded_hash}")

            # # Crop the image
            # image_crop_x: int = int(cropped_image_details["x"])
            # image_crop_y: int = int(cropped_image_details["y"])
            # image_crop_width: int = int(cropped_image_details["width"])
            # image_crop_height: int = int(cropped_image_details["height"])

            # logging.debug(f"image_crop_x: {image_crop_x}")
            # logging.debug(f"image_crop_y: {image_crop_y}")
            # logging.debug(f"image_crop_width: {image_crop_width}")
            # logging.debug(f"image_crop_height: {image_crop_height}")

            # # I prefer using less dependencies if possible so I used PIL instead.
            # profile_image_cropped = Image.open(profile_image)

            # # Crop image using Crop dimensions
            # profile_image_cropped = profile_image_cropped.crop(
            #     (image_crop_x, image_crop_y, image_crop_width + image_crop_x, image_crop_height + image_crop_y)
            # )

            # if user.profile_image_raw:
            #     # Check to see if the profile image is different from the current profile image

            #     if user.profile_image_raw_hash != profile_image_uploaded_hash:
            #         logging.debug("[ACCOUNTS.API.EDIT_UPDATE_PROFILE_IMAGE] Deleted old profile image")
            #         # Delete the old profile image
            #         user.profile_image_raw.delete()
            #         user.profile_image.delete()
            #         user.profile_image_thumbnail.delete()

            #         # Save the new profile image
            #         user.profile_image_raw = profile_image
            #         user.profile_image_raw_hash = profile_image_uploaded_hash
            #     else:
            #         logging.debug(
            #             "[ACCOUNTS.API.EDIT_UPDATE_PROFILE_IMAGE] Profile image is the same as the current profile image"
            #         )
            # else:
            #     user.profile_image_raw = profile_image
            #     user.profile_image_raw_hash = profile_image_uploaded_hash

        user.save()

        account_data = AccountPrivateDetailedSchema.from_orm(user)
        return 200, EditAccountResponseSchema(
            success=True, message="Settings successfully updated", account=account_data
        )
    else:
        logging.debug("[ACCOUNTS.API.EDIT_UPDATE_PROFILE_IMAGE] User is not authenticated")
        return 403, ErrorSchema(
            success=False,
            message="Unable to authenticate user",
        )


@accounts_router.post(
    "/auth/edit/user-notifications", auth=JWTAuth(), response={200: BaseResponseSchema, 403: ErrorSchema}
)
def edit_user_notifications_post(request, data: UpdateUserNotificationsSchema):
    logging.debug("[ACCOUNTS.API.EDIT_USER_NOTIFICATIONS] Called")
    user = request.user

    if user.is_authenticated:
        user.settings.receive_marketing_emails = data.receive_marketing_emails
        user.settings.receive_weekly_digest_emails = data.receive_weekly_digest_emails
        user.settings.receive_discovery_emails = data.receive_discovery_emails
        user.settings.receive_site_update_emails = data.receive_site_update_emails
        user.settings.receive_inbox_message_notifications = data.receive_inbox_message_notifications
        user.settings.receive_announcement_notifications = data.receive_announcement_notifications
        user.settings.save()

        return 200, BaseResponseSchema(
            success=True,
            message="Notification settings updated successfully",
        )

    else:
        logging.debug("[ACCOUNTS.API.EDIT_USER_NOTIFICATIONS] User is not authenticated")
        # HTTP Error 403: Server understood the request, but is unwilling to process it
        return 403, ErrorSchema(
            success=False,
            message="Unable update notification settings",
        )


@accounts_router.post("/auth/edit/delete-account", auth=JWTAuth(), response={200: BaseResponseSchema, 403: ErrorSchema})
def delete_account_post(request, data: DeleteUserRequestSchema):
    logging.debug("[ACCOUNTS.API.DELETE_ACCOUNT] Called")
    logging.debug(f"\tUser: {request.user}")

    user = request.user

    if user.is_authenticated:
        user_validated = False

        # Check that the UUID matches the user's UUID
        if str(user.uuid) == str(data.uuid):
            user_validated = True
        else:
            user_validated = False

        # Check that the user's email and password are correct
        authenticated = authenticate(email=user.email, password=data.password)
        if user_validated and authenticated:
            user_validated = True
        else:
            user_validated = False

        if user_validated:
            logging.debug("[ACCOUNTS.API.DELETE_ACCOUNT] User validated, deleting account")
            user.delete()
            return 200, BaseResponseSchema(
                success=True,
                message="Your account has been successfully deleted",
            )
        else:
            logging.debug("[ACCOUNTS.API.DELETE_ACCOUNT] User not validated")
            return 403, ErrorSchema(
                success=False,
                message="Account credentials are invalid, account was not deleted",
            )

    else:
        print("[ACCOUNTS.API.DELETE_ACCOUNT] User is not authenticated")
        # HTTP Error 403: Server understood the request, but is unwilling to process it
        return 403, ErrorSchema(
            success=False,
            message="Unable to authenticate user",
        )


@accounts_router.post(
    "/auth/edit/support-message", auth=JWTAuth(), response={200: BaseResponseSchema, 403: ErrorSchema}
)
def edit_user_send_support_message(request, data: SupportMessageRequestSchema):
    logging.debug("[ACCOUNTS.API.EDIT_USER_SEND_SUPPORT_MESSAGE] Called")
    user = request.user

    logging.debug(f"\tUser: {request.user}")
    logging.debug(f"\tData: {data}")

    try:
        if user.is_authenticated:
            # Get user
            user = request.user
        else:
            user = None

        support_message = SupportMessage.objects.create(
            name=data.name,
            user=user,
            email=data.email,
            page_url=data.page_url,
            subject=data.subject,
            content=data.content,
        )

        support_message.save()

        return 200, BaseResponseSchema(
            success=True,
            message="Notification settings updated successfully",
        )
    except Exception as e:
        logging.debug(
            "[ACCOUNTS.API.EDIT_USER_SEND_SUPPORT_MESSAGE] Error occurred while sending support message from user account page"
        )
        # HTTP Error 403: Server understood the request, but is unwilling to process it
        return 403, ErrorSchema(
            success=False,
            message="Unable update notification settings",
        )


# class UpdateAccountSchema(Schema):
#     first_name: str
#     last_name: str
#     # https://django-ninja.dev/guides/response/ says that FileField and ImageField should be a str
#     # profile_image: str


# @accounts_router.post("/upload")
# def upload(request, file: UploadedFile = File(...)):
#     print("[ACCOUNTS.API.UPLOAD] Called")
#     print(f"\tUser: {request.user}")
#     if file:
#         print(f"\tFile received: {file.name}, size: {len(file.read())}")
#     else:
#         print("\tNo file received")
#     return {}
