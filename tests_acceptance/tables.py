from sqlalchemy import Boolean, Column, Integer, String, select
import asyncio
from tests_acceptance.db import Model, Session, AsyncSession


class Films(Model):
    __tablename__ = "films"

    film_id = Column(Integer, primary_key=True)
    status = Column(String, index=True)
    title = Column(String)
    is_premiere = Column(Boolean)


# result = session.query(Films).first()
# user = await session.get(User, id)


class Pies(Model):
    __tablename__ = "pies"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(String)
    nutritional_value = Column(String)


async def _load_all(session1: AsyncSession):
    q = select(Pies, id=1)
    result = await session1.execute(q)
    curr = result.scalar()
    # curr = result.scalars()
    # for a1 in curr:
    #     print(a1)
    print(curr)

    # result = session1.query(Pies).first()
    # CACHE = {i.id: for i in curr}
    # return CACHE


async def main():
    async with Session() as session1:
        await _load_all(session1=session1)


# result = session.query(Pies).first()

if __name__ == "__main__":
    asyncio.run(main())
