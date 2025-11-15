from fastapi import APIRouter, Query, HTTPException, status
from fastapi.responses import JSONResponse
from backend.src.schemas import (
    TitleCreateSchema,
    TitleReadIDSchema,
    TitleReadAllSchema,
    TitleUpdateSchema,
)
from backend.src.dao.dao import TitleDAO
from typing import Annotated

title_router = APIRouter(prefix="/titles")


@title_router.get("")
async def get_all(
    page: Annotated[int, Query(ge=1)] = 1,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
):
    titles = await TitleDAO.get_all(page=page, limit=limit)
    res = [TitleReadAllSchema.model_validate(title).model_dump() for title in titles]
    return res


@title_router.get("/{title_id}")
async def get_by_id(title_id: int):
    title = await TitleDAO.get_by_id(model_id=title_id)
    if title:
        res = TitleReadIDSchema.model_validate(title).model_dump()
        return res
    raise HTTPException(status_code=404, detail="Publisher not found")


@title_router.post("")
async def add(title_data: TitleCreateSchema):
    title = await TitleDAO.add(values=title_data)
    return title


@title_router.patch("/{title_id}")
async def update_title(title_data: TitleUpdateSchema, title_id: int):
    title = await TitleDAO.update_by_id(values=title_data, model_id=title_id)
    return title


# @title_router.delete("")
# async def delete_title(title_ids: list[int]):
#     await TitleDAO.delete_one_or_many(model_ids=title_ids)
#     return JSONResponse(
#         status_code=status.HTTP_200_OK,
#         content={"detail": "The deletion was successful."},
#     )
