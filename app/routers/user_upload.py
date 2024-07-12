from fastapi import APIRouter

from ..models.db_util import User
router = APIRouter()


@router.post("/user/upload", tags=["user loading"])
async def user_upload(user_score: User):
    # Check if the username already exists
    # raise HTTPException(status_code=400, detail="Username already exists")

    # Save the user and their score
    return {"message": "User score saved successfully", "user_score": user_score}
