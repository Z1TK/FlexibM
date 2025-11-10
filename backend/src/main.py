from fastapi import FastAPI
from backend.src.author.author_router import author_router

app = FastAPI()

app.include_router(author_router)
