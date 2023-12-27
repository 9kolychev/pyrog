from fastapi.routing import APIRouter

from . import crud
from .schemas import CreateUser

router = APIRouter()


@router.post("/", response_model=dict)
async def create_user(user: CreateUser) -> dict:
    return crud.create_user(user_in=user)
