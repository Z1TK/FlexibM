from fastapi import APIRouter, HTTPException
from backend.src.database import connections
from sqlalchemy.ext.asyncio import AsyncSession
from backend.src.dao.dao import AuthorDAO
from backend.src.schemas import AuthorSchema

author_router = APIRouter(prefix="/authors")

@author_router.get('/{author_id}')
async def get_by_id(author_id: str):
    author = await AuthorDAO.get_by_id(
        model_id=author_id
    )
    if author:
        res = AuthorSchema.model_validate(author).model_dump()
        return res
    raise HTTPException(status_code=404, detail='Author not found')

@author_router.post("")
async def add_author(
    author_data: AuthorSchema,
):
    author = await AuthorDAO.add(
        values=author_data
        )
    if author:
        res = AuthorSchema.model_validate(author).model_dump()
        return res