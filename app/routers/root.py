from fastapi import APIRouter
router = APIRouter()


@router.get("/", tags=["root"])
async def read_root():
    return {"docs link": "http://127.0.0.1:8000/docs"}
