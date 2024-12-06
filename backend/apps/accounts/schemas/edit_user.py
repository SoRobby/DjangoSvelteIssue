from typing import List, Optional

from apps.accounts.models import Account, AccountSettings
from ninja import ModelSchema, Schema


class _AccountSettingsSchema(ModelSchema):
    class Meta:
        model = AccountSettings
        fields = "__all__"


# Get
class UserEditSchema(ModelSchema):
    settings: Optional[_AccountSettingsSchema] = None

    class Meta:
        model = Account
        fields = "__all__"
    
# Update
class UpdateUserGeneralSchema(Schema):
    first_name: str
    last_name: str
    bio: str
    organization: str
    position: str
    country_slug: str
    # cropped_image_details: Optional[str] = None

class UpdateUserProfileImageSchema(Schema):
    last_name: str
    cropped_image_details: Optional[str] = None

class UpdateUserNotificationsSchema(Schema):
    receive_marketing_emails: bool
    receive_weekly_digest_emails: bool
    receive_discovery_emails: bool
    receive_site_update_emails: bool
    receive_inbox_message_notifications: bool
    receive_announcement_notifications: bool


# Delete
class DeleteUserRequestSchema(Schema):
    password: str
    uuid: str