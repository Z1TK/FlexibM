from backend.src.dao.base_dao import BaseDAO
from backend.src.author.model import Author
from backend.src.publisher.model import Publisher
from backend.src.tag.model import Tag
from backend.src.genre.model import Genre
from backend.src.title.model import Title

class AuthorDAO(BaseDAO):
    model = Author

class PublisherDAO(BaseDAO):
    model = Publisher

class TitleDAO(BaseDAO):
    model = Title

class TagDAO(BaseDAO):
    model = Tag

class GenreDAO(BaseDAO):
    model = Genre