from fastapi import APIRouter

from ..models.db_util import User
router = APIRouter()


@router.get("/user/{uuid}/download", tags=["user loading"])
async def user_download(uuid: str):
    # Check if the username already exists
    # raise HTTPException(status_code=400, detail="Username already exists")

    # Save the user and their score
    return {"message": "User score saved successfully", "by id": uuid, "data": "-"}
