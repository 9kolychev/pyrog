from typing import Annotated

from fastapi import HTTPException, Depends, status, Path
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import db_helper
from . import crud
from db.models import Pie


async def pie_by_id(
    pie_id: Annotated[int, Path(ge=1, lt=1_000)],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Pie:
    pie = await crud.get_product(session=session, product_in=pie_id)
    if pie is not None:
        return pie

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Pie {pie_id} not found!",
    )
