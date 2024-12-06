from typing import List, Optional

from ninja import Schema


class EmailVerificationRequestSchema(Schema):
    token: str
