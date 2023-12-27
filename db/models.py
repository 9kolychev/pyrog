from sqlalchemy import Uuid

from sqlalchemy import Column, Boolean, String
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

import uuid


class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)


class User(Base):
    __tablename__ = "users"

    # user_id: Mapped[Uuid]
    # user_id: Mapped[str]
    name: Mapped[str]
    surname: Mapped[str]
    email: Mapped[str]
    # is_active: Mapped[bool]

    # user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # name = Column(String, nullable=False)
    # surname = Column(String, nullable=False)
    # email = Column(String, nullable=False, unique=True)
    # is_active = Column(Boolean(), default=True)
