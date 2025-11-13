from fastapi import FastAPI
from backend.src.author.author_router import author_router
from backend.src.publisher.publisher_router import publisher_router
from backend.src.tag.tag_router import tag_router
from backend.src.genre.genre_router import genre_router

app = FastAPI()

app.include_router(author_router)
app.include_router(publisher_router)
app.include_router(tag_router)
app.include_router(genre_router)
