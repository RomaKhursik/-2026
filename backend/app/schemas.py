from datetime import datetime

from pydantic import BaseModel


class TelemetryResponse(BaseModel):
    timestamp: datetime

    latitude: float
    longitude: float

    altitude_km: float
    velocity_km_s: float


class OrbitPoint(BaseModel):
    timestamp: datetime

    x_km: float
    y_km: float
    z_km: float

    vx_km_s: float
    vy_km_s: float
    vz_km_s: float