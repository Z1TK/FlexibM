from fastapi import APIRouter, Query
from backend.src.schemas import GenreReadSchema
from backend.src.dao.dao import GenreDAO
from typing import Annotated

genre_router = APIRouter(prefix='/genres')

@genre_router.get('')
async def get_all(
    page: Annotated[int, Query(ge=1)] = 1,
    limit: Annotated[int, Query(ge=1, gl=100)] = 10,
):
    genres = await GenreDAO.get_all(page=page, limit=limit)
    res = [GenreReadSchema.model_validate(genre).model_dump() for genre in genres]
    return res
