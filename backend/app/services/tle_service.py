from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import ISSTLE


def get_latest_tle(db: Session) -> ISSTLE | None:
    statement = (
        select(ISSTLE)
        .order_by(ISSTLE.published_at.desc())
        .limit(1)
    )

    return db.execute(statement).scalar_one_or_none()


def get_tle_for_time(
    db: Session,
    decision_time,
) -> ISSTLE | None:

    statement = (
        select(ISSTLE)
        .where(ISSTLE.published_at <= decision_time)
        .order_by(ISSTLE.published_at.desc())
        .limit(1)
    )

    return db.execute(statement).scalar_one_or_none()