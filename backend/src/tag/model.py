from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from backend.src.database import Base
# from backend.src.title.model import Title
from backend.src.association_tables import tag_title_table
import uuid
import slugify


class Tag(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    titles: Mapped[list["Title"]] = relationship(
        secondary=tag_title_table, back_populates="tags"
    )
