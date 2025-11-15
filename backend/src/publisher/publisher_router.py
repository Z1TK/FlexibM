from fastapi import APIRouter, HTTPException, Query, status
from fastapi.responses import JSONResponse
from typing import Annotated
from backend.src.dao.dao import PublisherDAO
from backend.src.schemas import PublisherCreateSchema, PublisherReadSchema, PublisherUpdateSchema

publisher_router = APIRouter(prefix='/publishers')

@publisher_router.get("")
async def get_all(
    page: Annotated[int, Query(ge=1)] = 1,
    limit: Annotated[int, Query(ge=1, gl=100)] = 10,
):
    publishers = await PublisherDAO.get_all(page=page, limit=limit)
    res = [PublisherReadSchema.model_validate(publisher).model_dump() for publisher in publishers]
    return res


@publisher_router.get("/{publisher_id}")
async def get_by_id(publisher_id: str):
    publisher = await PublisherDAO.get_by_id(model_id=publisher_id)
    if publisher:
        res = PublisherReadSchema.model_validate(publisher).model_dump()
        return res
    raise HTTPException(status_code=404, detail="Publisher not found")


@publisher_router.post("")
async def add_publisher(
    publisher_data: PublisherCreateSchema,
):
    publisher = await PublisherDAO.add(values=publisher_data)
    if publisher:
        res = PublisherReadSchema.model_validate(publisher).model_dump()
        return res


@publisher_router.patch("/{publisher_id}")
async def update_publisher(publisher_data: PublisherUpdateSchema, publisher_id: str):
    publisher = await PublisherDAO.update_by_id(model_id=publisher_id, values=publisher_data)
    if publisher:
        res = PublisherReadSchema.model_validate(publisher).model_dump()
        return res


@publisher_router.delete("")
async def delete_publisher(publisher_ids: list[str]):
    await PublisherDAO.delete_one_or_many(model_ids=publisher_ids)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"detail": "The deletion was successful."},
    )
