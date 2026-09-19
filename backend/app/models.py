# app/models.py
from datetime import datetime

from sqlalchemy import String, Float, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class ISSTLE(Base):
    __tablename__ = "iss_tle"

    id: Mapped[int] = mapped_column(primary_key=True)

    tle_line1: Mapped[str] = mapped_column(Text)
    tle_line2: Mapped[str] = mapped_column(Text)

    epoch_time: Mapped[datetime] = mapped_column(DateTime)
    published_at: Mapped[datetime] = mapped_column(DateTime)

    source: Mapped[str | None] = mapped_column(String(100), nullable=True)


class SpaceWeather(Base):
    __tablename__ = "space_weather"

    id: Mapped[int] = mapped_column(primary_key=True)

    timestamp: Mapped[datetime] = mapped_column(DateTime)

    kp_index: Mapped[float | None] = mapped_column(Float, nullable=True)
    proton_flux: Mapped[float | None] = mapped_column(Float, nullable=True)
    xray_flux: Mapped[float | None] = mapped_column(Float, nullable=True)

    published_at: Mapped[datetime] = mapped_column(DateTime)

    source: Mapped[str | None] = mapped_column(String(100), nullable=True)


class DebrisConjunction(Base):
    __tablename__ = "debris_conjunctions"

    id: Mapped[int] = mapped_column(primary_key=True)

    object_name: Mapped[str] = mapped_column(String(200))

    tca_time: Mapped[datetime] = mapped_column(DateTime)

    miss_distance_km: Mapped[float] = mapped_column(Float)

    published_at: Mapped[datetime] = mapped_column(DateTime)

    source: Mapped[str | None] = mapped_column(String(100), nullable=True)