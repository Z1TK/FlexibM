from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from backend.src.database import Base
from backend.src.association_tables import genre_title_table


class Genre(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    titles: Mapped[list["Title"]] = relationship(
        secondary=genre_title_table, back_populates="genres"
    )
