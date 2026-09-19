from fastapi import FastAPI

from app.database import Base, engine

from api.health import router as health_router
from api.orbit import router as orbit_router
from api.telemetry import router as telemetry_router
from api.risks import router as risks_router
from api.windows import router as windows_router
from api.replay import router as replay_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="CosmoHackathon 2026",
    description="ISS EVA Decision Support System",
    version="0.1.0",
)


app.include_router(health_router)
app.include_router(orbit_router)
app.include_router(telemetry_router)
app.include_router(risks_router)
app.include_router(windows_router)
app.include_router(replay_router)