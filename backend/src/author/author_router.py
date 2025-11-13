from fastapi import APIRouter, HTTPException, Query, status
from fastapi.responses import JSONResponse
from typing import Annotated
from backend.src.dao.dao import AuthorDAO
from backend.src.schemas import AuthorCreateSchema, AuthorReadSchema

author_router = APIRouter(prefix="/authors")


@author_router.get("")
async def get_all(
    page: Annotated[int, Query(ge=1)] = 1,
    limit: Annotated[int, Query(ge=1, gl=100)] = 10,
):
    authors = await AuthorDAO.get_all(page=page, limit=limit)
    res = [AuthorReadSchema.model_validate(author).model_dump() for author in authors]
    return res


@author_router.get("/{author_id}")
async def get_by_id(author_id: str):
    author = await AuthorDAO.get_by_id(model_id=author_id)
    if author:
        res = AuthorReadSchema.model_validate(author).model_dump()
        return res
    raise HTTPException(status_code=404, detail="Author not found")


@author_router.post("")
async def add_author(
    author_data: AuthorCreateSchema,
):
    author = await AuthorDAO.add(values=author_data)
    if author:
        res = AuthorReadSchema.model_validate(author).model_dump()
        return res


@author_router.patch("{author_id}")
async def update_author(author_data: AuthorCreateSchema, author_id: str):
    author = await AuthorDAO.update_by_id(model_id=author_id, values=author_data)
    if author:
        res = AuthorReadSchema.model_validate(author).model_dump()
        return res


@author_router.delete("")
async def delete_authors(author_ids: list[str]):
    await AuthorDAO.delete_one_or_many(model_ids=author_ids)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"detail": "The deletion was successful."},
    )
