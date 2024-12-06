from typing import Literal, Optional

from pydantic import BaseModel


# Note pydnaic BaseResponseSchema is used to create a schema because it allows for "extra" fields to be passed in the request
class BaseResponseSchema(BaseModel):
    success: bool
    message: Optional[str] = None

    class Config:
        # Allows extra fields to be passed in the request
        extra = "allow"


# OLD CODE FOR REFERENCE
# from ninja import Schema
# class BaseSchema(Schema):
#     success: bool
#     status: Literal["success", "error", "fail"]
#     message: Optional[str] = None

#     class Config:
#         extra = "allow"  # Allows extra fields to be passed in the request
