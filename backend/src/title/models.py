from sqlalchemy.orm import Mapped, mapped_column, validates
from sqlalchemy import ForeignKey, Text, event, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from backend.src.database import Base
from backend.src.sql_enum import *
import uuid
import slugify


class Title(Base):
    id: Mapped[str] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String(255))
    slug: Mapped[str] = mapped_column(String(255), unique=True)
    description: Mapped[str] = mapped_column(Text)
    alternative_title: Mapped[str] = mapped_column(
        String(255), nullable=True, unique=True
    )
    release_year: Mapped[int] = mapped_column(Integer)
    type: Mapped[TypeEnum] = mapped_column(default="manga")
    status: Mapped[StatusEnum] = mapped_column(default="ongoing")
    release_format: Mapped[ReleaseEnum] = mapped_column(nullable=True)

    @validates("release_year")
    def validate_release_year(self, key, year):
        if year <= 0:
            raise ValueError("release_year must be positive")
        return year