from typing import Optional

from ninja import Schema


class FeedbackMessageRequestSchema(Schema):
    name: Optional[str] = None
    email: Optional[str] = None
    page_url: Optional[str] = None
    content: str

