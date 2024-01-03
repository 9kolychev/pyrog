from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.session import db_helper
from . import crud
from .schemas import Profile, CreateProfile

router = APIRouter()


# @router.get("/", response_model=Profile)
# async def get_profile():
#     pass


@router.post(
    "/",
    response_model=Profile,
    status_code=status.HTTP_201_CREATED,
)
async def create_profile(
    profile_in: CreateProfile,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_profile(
        session=session,
        profile=profile_in,
    )
