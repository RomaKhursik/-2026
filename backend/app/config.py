# app/config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = (
        "postgresql+psycopg2://postgres:postgres@localhost:5432/cosmo"
    )

    iss_norad_id: int = 25544

    orbit_step_seconds: int = 60
    telemetry_step_seconds: int = 60

    weather_weight: float = 0.6
    debris_weight: float = 0.4

    class Config:
        env_file = ".env"


settings = Settings()