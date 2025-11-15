from backend.src.dao.base_dao import BaseDAO
from backend.src.author.model import Author
from backend.src.publisher.model import Publisher
from backend.src.tag.model import Tag
from backend.src.genre.model import Genre
from backend.src.title.model import Title
from backend.src.database import connection
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from pydantic import BaseModel


class AuthorDAO(BaseDAO[Author]):
    model = Author


class PublisherDAO(BaseDAO[Publisher]):
    model = Publisher


class TitleDAO(BaseDAO[Title]):
    model = Title

    @classmethod
    @connection
    async def get_by_id(cls, session: AsyncSession, model_id: int):
        query = (
            select(cls.model)
            .options(
                selectinload(cls.model.author),
                selectinload(cls.model.publisher),
                selectinload(cls.model.genres),
                selectinload(cls.model.tags),
            )
            .filter_by(id=model_id)
        )
        result = await session.execute(query)
        info_one = result.scalar_one_or_none()
        return info_one

    @classmethod
    @connection
    async def add(cls, session: AsyncSession, values: BaseModel):
        values = values.model_dump(exclude_unset=True)

        genre_ids = values.pop("genres", [])
        genres = await GenreDAO.get_by_ids(ids=genre_ids)

        tag_ids = values.pop("tags", [])
        tags = await TagDAO.get_by_ids(ids=tag_ids)

        author_id = values.pop("author_id")
        author = await AuthorDAO.get_by_id(model_id=author_id)

        publisher_id = values.pop("publisher_id")
        publisher = await PublisherDAO.get_by_id(model_id=publisher_id)

        new_title = cls.model(**values)
        new_title.genres.extend(genres)
        new_title.tags.extend(tags)
        new_title.author = author
        new_title.publisher = publisher

        session.add(new_title)
        try:
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e
        return new_title


class TagDAO(BaseDAO[Tag]):
    model = Tag


class GenreDAO(BaseDAO[Genre]):
    model = Genre
