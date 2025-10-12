from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text, event, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from backend.src.database import Base
import uuid
import slugify


class Publisher(Base):
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(255), unique=True)
    slug: Mapped[str] = mapped_column(String(255), unique=True)
    another_name: Mapped[str] = mapped_column(String, unique=True, nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    image: Mapped[str] = mapped_column(String(255), nullable=True)
    titles: Mapped[list["Title"]] = relationship(
        "Title", back_populates="publisher", cascade="all, delete-orphan"
    )
