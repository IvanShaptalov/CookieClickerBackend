from fastapi import APIRouter
from ..models import db_methods

router = APIRouter()


@router.get("/user/{uuid}", tags=["user"])
async def get_user_by_id(user_id: str):
    user = await db_methods.get_user_by_id(user_id=user_id)
    if user is None:
        return {"user not found": 200}
    return {"user": user}
