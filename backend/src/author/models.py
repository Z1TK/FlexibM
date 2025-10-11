from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Text, event, String
from sqlalchemy.dialects.postgresql import UUID
from backend.src.database import Base
import uuid
import slugify


class Author(Base):
    id: Mapped[str] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(255), unique=True)
    slug: Mapped[str] = mapped_column(String(255), unique=True)
    pseodunym: Mapped[str] = mapped_column(String(255), unique=True, nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    image: Mapped[str] = mapped_column(String(255), nullable=True)

    @event.listens_for(Author, "before_insert")
    @event.listens_for(Author, "before_update")
    def generate_slug(Mapper, connection, target):
        if target.name:
            target.slug = slugify(target.name, lowercase=True)
