from typing import Optional

from ninja import Schema


class SupportMessageRequestSchema(Schema):
    name: str
    email: str
    username: Optional[str] = None
    page_url: Optional[str] = None
    subject: Optional[str] = None
    content: str



# class UserSettingsSupportSchema(Schema):
#     name: str
#     username: str
#     email: str
#     subject: str
#     message: str


