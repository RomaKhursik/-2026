from datetime import datetime, timezone

from sgp4.api import Satrec
from sgp4.api import jday


def create_satellite(tle_line1: str, tle_line2: str) -> Satrec:
    return Satrec.twoline2rv(
        tle_line1,
        tle_line2,
    )


def propagate(
    satellite: Satrec,
    timestamp: datetime,
) -> dict:

    if timestamp.tzinfo is None:
        timestamp = timestamp.replace(tzinfo=timezone.utc)

    timestamp = timestamp.astimezone(timezone.utc)

    jd, fr = jday(
        timestamp.year,
        timestamp.month,
        timestamp.day,
        timestamp.hour,
        timestamp.minute,
        timestamp.second + timestamp.microsecond / 1_000_000,
    )

    error, position, velocity = satellite.sgp4(jd, fr)

    if error != 0:
        raise RuntimeError(
            f"SGP4 error code: {error}"
        )

    return {
        "timestamp": timestamp,
        "x_km": position[0],
        "y_km": position[1],
        "z_km": position[2],
        "vx_km_s": velocity[0],
        "vy_km_s": velocity[1],
        "vz_km_s": velocity[2],
    }
ISS_TLE = {
    "name": "ISS",
    "line1": "1 25544U 98067A   26090.50000000  .00010000  00000-0  18000-3 0  9999",
    "line2": "2 25544  51.6400 100.0000 0005000 200.0000 160.0000 15.50000000123456"
}
def get_iss_tle():
    return ISS_TLE