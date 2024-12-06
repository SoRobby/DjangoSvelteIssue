# from ninja import File, NinjaAPI, Schema
# from ninja.responses import Response

# from apps.accounts.models import Account
# from apps.core.schemas import ErrorDetailsSchema, ErrorSchema
# from apps.feedback.models import SupportMessage

# from .router import feedback_router


# @feedback_router.post("/support/messages")
# def support_messages(request, data: SupportMessagesPostSchema):
#     print("[FEEDBACK.API.SUPPORT_MESSAGES POST] Called")

#     print(f'Data: {data}')

#     if request.user:
#         print('User is logged in')
#         # Attempt to get user by username
#         SupportMessage.objects.create(
#             name=data.name,
#             user=request.user,
#             email=data.email,
#             subject=data.subject,
#             content=data.content,
#             page_url=data.page_url
#         )
#     else:
#         print('User is not logged in')
#         SupportMessage.objects.create(
#             name=data.name,
#             email=data.email,
#             subject=data.subject,
#             content=data.content,
#             page_url=data.page_url
#         )

#     print(f"\tUser: {request.user}")
#     print(f"\tData: {data}")
    
#     return {}