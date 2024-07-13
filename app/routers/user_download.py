from fastapi import APIRouter, HTTPException, status, Response
from ..models import db_methods
from ..models.db_util import engine
from ..models.db_errors import *
import json
router = APIRouter()


@router.get("/user/{uuid}/download", tags=["user loading"])
async def user_download(user_id: str):
    try:
        async with engine.begin() as session:
            user = await db_methods.get_user_by_id(user_id=user_id, session=session)
            if user is None:
                raise UserNotFoundError()
    except UserNotFoundError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
    return Response(content=json.dumps(user.model_dump()), status_code=status.HTTP_200_OK)
