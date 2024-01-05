"""
# For learn sqlite

import sqlite3 as sq

con = sq.connect("saper.db")
cur = con.cursor()

cur.execute("")

con.close()
"""

import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from db.models import db_helper, User, Profile, Pie


async def create_user(session: AsyncSession, username: str) -> User:
    user = User(username=username)
    session.add(user)
    await session.commit()
    print("user", user)
    return user


async def main():
    async with db_helper.session_factory() as session:
        await create_user(session=session, username="John")
        await create_user(session=session, username="Sam")


if __name__ == "__main__":
    asyncio.run(main())
