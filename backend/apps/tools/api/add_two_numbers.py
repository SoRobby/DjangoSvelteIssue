import logging
from typing import Any, Optional

import numpy as np
from apps.core.schemas import BaseResponseSchema
from apps.tools.api.router import tools_router
from apps.tools.schemas import OutputValueSchema, UnitsSchema
from ninja import Query, Schema


# Define the schema
class AddTwoNumbersResponseSchema(Schema):
    # Note schema also controls the order of the output
    result: OutputValueSchema


# Define the api endpoint(s)


@tools_router.get("/tools/add-two-numbers", response={200: BaseResponseSchema})
def add_numbers_get(request, value_a: Query[Any], value_b: Query[Any]):
    logging.debug(f"[TOOLS.API] add_numbers_get()")

    # Ensure values are properly formatted for calculation
    a = float(value_a)
    b = float(value_b)

    logging.debug(f"Value A: {a}")
    logging.debug(f"Value B: {b}")

    return 200, BaseResponseSchema(
        success=True,
        outputs=AddTwoNumbersResponseSchema(
            result=OutputValueSchema(
                name="Power generated at Earth",
                value=a + b,
                units=UnitsSchema(prefix="", suffix=""),
                tooltip="Value of A + B, added together.",
            )
        ),
    )
