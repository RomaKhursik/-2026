from fastapi import APIRouter


router = APIRouter(
    prefix="/api/windows",
    tags=["Windows"],
)


@router.get("/")
def get_windows():
    return {
        "status": "not_implemented"
    }