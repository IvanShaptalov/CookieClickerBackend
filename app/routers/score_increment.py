from fastapi import APIRouter
router = APIRouter()


@router.get("/score/increment/{uuid}", tags=["score"])
async def increment_score(uuid: str):
    return {"user_id": uuid}
