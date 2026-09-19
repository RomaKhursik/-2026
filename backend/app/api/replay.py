from fastapi import APIRouter


router = APIRouter(
    prefix="/api/replay",
    tags=["Replay"],
)


@router.get("/")
def replay():
    return {
        "status": "not_implemented"
    }