from fastapi import APIRouter
router = APIRouter()


@router.get("/users/{uuid}", tags=["user"])
async def read_user(uuid: str):
    return {"user_id": uuid}
