from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Pie

from .schemas import CreatePie, UpdatePie, UpdatePiePartial


async def get_products(session: AsyncSession) -> list[Pie]:
    stmt = select(Pie).order_by(Pie.id)
    result: Result = await session.execute(stmt)
    pies = result.scalars().all()
    return list(pies)


async def get_product(session: AsyncSession, product_in: int) -> Pie | None:
    return await session.get(Pie, product_in)


async def create_product(session: AsyncSession, product: CreatePie) -> Pie:
    pie = Pie(**product.model_dump())
    session.add(pie)
    await session.commit()
    return pie


async def update_product(
    session: AsyncSession,
    product: Pie,
    product_update: UpdatePie | UpdatePiePartial,
    partial: bool = False,
) -> Pie:
    for key, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, key, value)
    await session.commit()
    return product


async def delete_product(session: AsyncSession, product: Pie) -> None:
    await session.delete(product)
