from fastapi import APIRouter


router = APIRouter(
    prefix="/api/risks",
    tags=["Risks"],
)


@router.get("/")
def get_risks():
    return {
        "status": "not_implemented"
    }