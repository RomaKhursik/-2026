from datetime import datetime, timezone
from math import sqrt

from services.orbit_service import propagate


EARTH_RADIUS_KM = 6378.137


def calculate_telemetry(
    satellite,
    timestamp: datetime,
) -> dict:

    point = propagate(
        satellite,
        timestamp,
    )

    x = point["x_km"]
    y = point["y_km"]
    z = point["z_km"]

    vx = point["vx_km_s"]
    vy = point["vy_km_s"]
    vz = point["vz_km_s"]

    distance_from_center = sqrt(
        x * x +
        y * y +
        z * z
    )

    altitude = (
        distance_from_center -
        EARTH_RADIUS_KM
    )

    velocity = sqrt(
        vx * vx +
        vy * vy +
        vz * vz
    )

    return {
        "timestamp": point["timestamp"],

        # Пока это орбитальные координаты.
        # Географические lat/lon добавим следующим этапом.
        "x_km": x,
        "y_km": y,
        "z_km": z,

        "altitude_km": altitude,
        "velocity_km_s": velocity,
    }