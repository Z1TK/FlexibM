from fastapi import APIRouter, Query
from backend.src.schemas import TagReadSchema
from backend.src.dao.dao import TagDAO
from typing import Annotated

tag_router = APIRouter(prefix='/tags')

@tag_router.get('')
async def get_all(
    page: Annotated[int, Query(ge=1)] = 1,
    limit: Annotated[int, Query(ge=1, gl=100)] = 10,
):
    tags = await TagDAO.get_all(page=page, limit=limit)
    res = [TagReadSchema.model_validate(tag).model_dump() for tag in tags]
    return res