from .author import (
    AuthorCreateSchema,
    AuthorIdSchema,
    AuthorReadSchema,
    AuthorUpdateSchema,
)
from .genre import GenreReadSchema
from .tag import TagReadSchema
from .publisher import (
    PublisherCreateSchema,
    PublisherIdschema,
    PublisherReadSchema,
    PublisherUpdateSchema,
)
from .title import (
    TitleCreateSchema,
    TitleReadAllSchema,
    TitleReadIDSchema,
    TitleUpdateSchema,
)

AuthorIdSchema.model_rebuild()
PublisherIdschema.model_rebuild()
TitleReadIDSchema.model_rebuild()
