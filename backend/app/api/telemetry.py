from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.databace import get_db
from services.tle_service import get_latest_tle
from services.orbit_service import create_satellite
from services.telemetry_service import calculate_telemetry


router = APIRouter(
    prefix="/api/telemetry",
    tags=["Telemetry"],
)


@router.get("/iss")
def get_iss_telemetry(
    db: Session = Depends(get_db),
):

    tle = get_latest_tle(db)

    if tle is None:
        raise HTTPException(
            status_code=404,
            detail="TLE for ISS not found",
        )

    satellite = create_satellite(
        tle.tle_line1,
        tle.tle_line2,
    )

    now = datetime.now(timezone.utc)

    telemetry = calculate_telemetry(
        satellite,
        now,
    )

    return telemetry