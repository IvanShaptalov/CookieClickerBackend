from ..models.db_util import User
from ..models import db_methods
from fastapi import APIRouter, HTTPException, status, Response
from ..models.db_errors import *
from ..models.db_util import engine
import json
router = APIRouter()


@router.post("/score/increment", tags=["score"], response_model=User | None)
async def increment_score(user_id: str, score: int):
    try:
        async with engine.begin() as session:
            user = await db_methods.increment_score(user_id=user_id, score=score, session=session)
    except UserNotFoundError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
    return Response(content=json.dumps(user.model_dump()), status_code=status.HTTP_200_OK)
