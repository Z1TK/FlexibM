from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import Text, String, Integer
from backend.src.sql_enum import *
import uuid
from typing import Annotated

class AuthorCreateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Annotated[str, Field(String(255))]
    pseodunym: Annotated[str | None, Field(String(255))]
    description: Annotated[str | None, Field(Text())]
    image: Annotated[str | None, Field(String(2048))]

class AuthorReadSchema(AuthorCreateSchema):
    model_config = ConfigDict(from_attributes=True)

    id: Annotated[uuid.UUID, Field()]

class PublisherCreateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Annotated[str, Field(String(255))]
    another_name: Annotated[str | None, Field(String(255))]
    description: Annotated[str | None, Field(Text())]
    image: Annotated[str | None, Field(String(2048))]

class PublisherReadSchema(PublisherCreateSchema):
    model_config = ConfigDict(from_attributes=True)

    id: Annotated[uuid.UUID, Field()]

class TitleCreateSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        use_enum_values=True
        )

    title: Annotated[str, Field(String(255))]
    description: Annotated[str, Field(Text())]
    alternative_name: Annotated[str | None, Field(String(255))]
    cover: Annotated[str, Field(String(255))]
    release_year: Annotated[int, Field(Integer)]
    type: Annotated[TypeEnum, Field()]
    status: Annotated[StatusEnum, Field()]
    release_format: Annotated[ReleaseEnum, Field()]
    author_id: Annotated[uuid.UUID, Field()]
    publisher_id: Annotated[uuid.UUID, Field()] 
    genres: Annotated[list[int], Field()]
    tags: Annotated[list[int], Field()]

class TitleReadSchema(TitleCreateSchema):
    model_config = ConfigDict(
        from_attributes=True,
        use_enum_values=True
    )

    id: Annotated[uuid.UUID, Field()]

class GenreReadSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: Annotated[int, Field()]
    name: Annotated[str, Field(String(255))]

class TagReadSchema(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )
    
    id: Annotated[int, Field()]
    name: Annotated[str, Field(String(255))]
