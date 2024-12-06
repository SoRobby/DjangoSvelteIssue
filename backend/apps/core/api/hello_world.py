# from apps.core.schemas import ErrorSchema
import logging
from typing import Union

from apps.core.models import Country
from apps.core.schemas import (
    BaseResponseSchema,
    CountryBasicSchema,
    Error400Schema,
    ErrorSchema,
)
from apps.supplier.models import Supplier, SupplierFile
from django.http import HttpRequest
from ninja import Schema

from .router import core_router


class Data(Schema):
    content: str


@core_router.get("/hello-world", response={200: BaseResponseSchema})
def hello_world_get(request: HttpRequest):
    logging.debug("[CORE.API.HELLO_WORLD_GET] Called")

    countries = Country.objects.all()[0:3]
    country_data = [CountryBasicSchema.from_orm(country) for country in countries]

    # Change BaseSchema to the schema you want to use for the response
    return 200, BaseResponseSchema(
        success=True,
        message="Request was successful",
        # Example of adding extra fields to the response
        chicken="Chicken was crossing the road...",  # type: ignore
        turkey={"turkey": "Turkey was crossing the road..."},  # type: ignore
        countries=country_data,  # type: ignore
    )


@core_router.post("/hello-world", response={200: BaseResponseSchema, 403: ErrorSchema})
def hello_world_post(request: HttpRequest, data: Data):
    logging.debug("[CORE.API.HELLO_WORLD_POST] Called")
    logging.debug(f"[CORE.API.HELLO_WORLD_POST] Data: {data}")
    try:
        return 200, BaseResponseSchema(
            success=True,
            message="Post request successful",
        )

    except Exception as e:
        logging.error(f"[CORE.API.HELLO_WORLD_POST] Error: {e}")
        return 403, ErrorSchema(
            success=False,
            message="Unable to process request!",
        )


@core_router.post(
    "/hello-world-response-test", response={200: BaseResponseSchema, 204: BaseResponseSchema, 403: ErrorSchema}
)
def response_test(request: HttpRequest, data: Data):
    logging.debug("[CORE.API.HELLO_POST] Called")
    logging.debug(f"[CORE.API.HELLO_POST] Data: {data}")

    if data.content == "200-single-country":
        logging.debug("[CORE.API.HELLO_POST] 200 success")
        country = Country.objects.first()
        country_data = CountryBasicSchema.from_orm(country)

        return 200, BaseResponseSchema(
            success=True, message="Request was successful", country=country_data  # type: ignore
        )

    elif data.content == "200-list-countries":
        logging.debug("[CORE.API.HELLO_POST] 200 success")
        countries = Country.objects.all()
        country_data = [CountryBasicSchema.from_orm(country) for country in countries]
        return 200, BaseResponseSchema(
            success=True,
            message="Post request successful",
            countries=country_data,  # type: ignore
        )

    elif str(data.content) == "204":
        # 204 No content response
        logging.debug("[CORE.API.HELLO_POST] 204 success")
        return 204, None

    elif data.content == "400":
        # HTTP Error 400: The server cannot or will not process the request due to an apparent client error
        logging.debug("[CORE.API.HELLO_POST] 400 error")
        return 400, ErrorSchema(
            success=False,
            message="The server cannot or will not process the request due to an apparent client error",
        )

    elif data.content == "403":
        logging.debug("[CORE.API.HELLO_POST] 403 error")
        return 403, ErrorSchema(
            success=False,
            message="Unable to process request!",
            errors=[
                Error400Schema(field="content1", message="The content1 field is invalid"),
                Error400Schema(field="content2", message="The content2 field is invalid"),
            ],
        )

    elif data.content == "500":
        # This will purposely cause a server error
        logging.debug("[CORE.API.HELLO_POST] 500 error")
        a = 1 / 0

    else:
        logging.debug("[CORE.API.HELLO_POST] Default response")
        return 200, BaseResponseSchema(
            success=True,
            message="Post request successful",
        )


@core_router.post("/hello-world-file-upload", response={200: BaseResponseSchema, 403: ErrorSchema})
def hello_world_file_upload(request: HttpRequest):
    logging.debug("[CORE.API.HELLO_WORLD_FILE_UPLOAD] Called")
    logging.debug(f"[CORE.API.HELLO_WORLD_FILE_UPLOAD] Data:")

    # print all data
    for key, value in request.POST.items():
        logging.debug(f"[CORE.API.HELLO_WORLD_FILE_UPLOAD] {key}: {value}")


    try:
        return 200, BaseResponseSchema(
            success=True,
            message="Post request successful",
        )

    except Exception as e:
        logging.error(f"[CORE.API.HELLO_WORLD_POST] Error: {e}")
        return 403, ErrorSchema(
            success=False,
            message="Unable to process request!",
        )