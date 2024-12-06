from typing import Optional

import numpy as np
from apps.tools.api.router import tools_router
from apps.tools.schemas import OutputValueSchema, UnitsSchema
from libs.spacelib.constants import SOLAR_CONSTANT
from ninja import Query, Schema


# Define the schema
class SolarArrayPowerGenerationSchema(Schema):
    # Note schema also controls the order of the output
    power_generation_at_earth: OutputValueSchema
    power_generation_at_distance: OutputValueSchema
    ratio: OutputValueSchema


# Define the api endpoint(s)
@tools_router.get("/tools/solar-array-power-generation", response=SolarArrayPowerGenerationSchema)
def solar_array_power_generation(
    request,
    distance: float = Query(...),
    effective_area: float = Query(...),
    cell_efficiency: float = Query(...),
    incidence_angle: float = Query(...),
):
    """
    Returns solar array power generation as a function of distance, panel effective area and efficiency, and sun incidence angle relative to the panel.

    INPUT:
    - distance              (AU)            = Distance from the sun.
    - effective_area        (W)             = Solar panel, area that is capable of generating power.
    - efficiency            (fraction)      = Solar panel cell power generation efficiency.
    - incidence_angle       (deg)           = Angle between a ray incident on a surface and the line perpendicular to the surface at the point of incidence

    OUTPUT:
    - power_gen_earth       (W)             = Power generated at Earth or 1 AU.
    - power_gen_distance    (W)             = Power generated at the input distance.

    SOURCE:
    - Space Mission Engineering: The New SMAD (Space Technology Library, Vol. 28)
    """
    print(f"[TOOLS.API] solar_array_power_generation()")

    ratio = 1.0 / (distance**2)

    power_gen_earth = SOLAR_CONSTANT * effective_area * cell_efficiency * np.cos(np.deg2rad(incidence_angle))

    power_gen_distance = ratio * power_gen_earth

    return SolarArrayPowerGenerationSchema(
        power_generation_at_earth=OutputValueSchema(
            name="Power generated at Earth",
            value=power_gen_earth,
            units=UnitsSchema(prefix="", suffix="W"),
            tooltip="Power generated at Earth or 1 AU.",
        ),
        power_generation_at_distance=OutputValueSchema(
            name="Power generated at distance",
            value=power_gen_distance,
            units=UnitsSchema(prefix="", suffix="W"),
            tooltip="Power generated at the input distance.",
        ),
        ratio=OutputValueSchema(
            name="Ratio",
            value=ratio,
            units=UnitsSchema(prefix="", suffix=""),
            tooltip="Ratio of power generated at the input distance to power generated at Earth.",
        ),
    )
