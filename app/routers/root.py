from fastapi import APIRouter, status, Response
import json
router = APIRouter()


@router.get("/", tags=["root"])
async def read_root():
    return Response(status_code=status.HTTP_200_OK, content=json.dumps({"docs link": "http://127.0.0.1:8000/docs"}))
