from ..models.db_util import User
from ..models import db_methods
from fastapi import APIRouter, HTTPException, status, Response
from ..models.db_errors import *
from ..models.db_util import engine
import json


router = APIRouter()


@router.post("/user/create", tags=["user"], status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user_endpoint(user: User):
    try:
        async with engine.begin() as session:
            result = await db_methods.create_user(user, session)

    except UserAlreadyExists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exist")

    except DatabaseError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad request")

    return Response(content=json.dumps({"user created": result.model_dump()}), status_code=status.HTTP_201_CREATED)
