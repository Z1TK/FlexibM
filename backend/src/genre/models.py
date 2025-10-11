from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from backend.src.database import Base


class Genre(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
