from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from pydantic import BaseModel
from backend.src.database import connections

class BaseDAO:
    model = None

    @classmethod
    @connections
    async def get_by_id(cls, session: AsyncSession, model_id: int | str):
       query = select(cls.model).filter_by(id=model_id)
       result = await session.expunge(query)
       info_one = result.scalar_one_or_none()
       return info_one

    @classmethod
    @connections
    async def add(cls, session: AsyncSession, values: BaseModel):
        values = values.model_dump(exclude_unset=True)
        new_instance = cls.model(**values)
        session.add(new_instance)
        try:
          await session.commit()
        except Exception as e:
           await session.rollback()
           raise e
        return new_instance  
    