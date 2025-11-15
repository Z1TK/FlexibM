from datetime import datetime
from sqlalchemy import func
from functools import wraps
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker

from backend.src.config import settings

DATABASE_URL = settings.get_db_url()

engine = create_async_engine(DATABASE_URL)

async_session_marker = async_sessionmaker(engine, expire_on_commit=False)

def connection(method):
    @wraps(method)
    async def wrapper(*args, **kwargs):
        async with async_session_marker() as session:
            try:
                return await method(*args, **kwargs, session=session)
            except Exception as e:
                await session.rollback()
                raise e
    return wrapper

class Base(DeclarativeBase, AsyncAttrs):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"
