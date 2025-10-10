from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker

from config import settings

DATABASE_URL = settings.get_db_url()

engine = create_async_engine(DATABASE_URL)

async_session_marker = async_sessionmaker(engine, expire_on_commit=False) 

class Base(DeclarativeBase, AsyncAttrs):
    abstract = True

    @declared_attr.directive
    def tablename(cls) -> str:
        return cls.name.lower() + 's'