from sqlalchemy import Column, Table, ForeignKey
from backend.src.database import Base

genre_title_table = Table(
    "genre_title_table",
    Base.metadata,
    Column("genre_id", ForeignKey("genres.id"), primary_key=True),
    Column("title_id", ForeignKey("titles.id"), primary_key=True),
)

tag_title_table = Table(
    "tag_title_table",
    Base.metadata,
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
    Column("title.id", ForeignKey("titles.id"), primary_key=True),
)
