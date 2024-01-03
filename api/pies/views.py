from fastapi import APIRouter, Depends, status, Security, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from auth import utils as auth_utils
from db.models.session import db_helper
from . import crud
from .schemas import Pie, CreatePie, UpdatePie
from .dependencies import pie_by_id


router = APIRouter()

security = HTTPBearer()


@router.get("/", response_model=list[Pie])
async def get_pies(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_products(session=session)


@router.post(
    "/",
    response_model=Pie,
    status_code=status.HTTP_201_CREATED,
)
async def create_pie(
    pie_in: CreatePie,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    credentials: HTTPAuthorizationCredentials = Security(security),
):
    token = credentials.credentials
    if auth_utils.decode_jwt(token):
        return await crud.create_product(
            session=session,
            product=pie_in,
        )


@router.get("/{pie_id}/", response_model=Pie)
async def get_pie_by_id(
    pie: Pie = Depends(pie_by_id),
):
    return pie


@router.put("/{pie_id}/")
async def update_pie(
    pie_update: UpdatePie,
    pie: Pie = Depends(pie_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    credentials: HTTPAuthorizationCredentials = Security(security),
) -> Pie:
    token = credentials.credentials
    if auth_utils.decode_jwt(token):
        return await crud.update_product(
            session=session,
            product=pie,
            product_update=pie_update,
        )


@router.put("/{pie_id}/")
async def update_pie_partial(
    pie_update: UpdatePie,
    pie: Pie = Depends(pie_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    credentials: HTTPAuthorizationCredentials = Security(security),
) -> Pie:
    token = credentials.credentials
    if auth_utils.decode_jwt(token):
        return await crud.update_product(
            session=session,
            product=pie,
            product_update=pie_update,
            partial=True,
        )


@router.delete("/{pie_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    pie: Pie = Depends(pie_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    credentials: HTTPAuthorizationCredentials = Security(security),
) -> None:
    token = credentials.credentials
    if auth_utils.decode_jwt(token):
        await crud.delete_product(
            session=session,
            product=pie,
        )
