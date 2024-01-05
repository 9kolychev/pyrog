from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Profile
from .schemas import CreateProfile


async def create_profile(
    session: AsyncSession,
    profile: CreateProfile,
) -> Profile:
    profile = Profile(**profile.model_dump())
    session.add(profile)
    await session.commit()
    return profile
