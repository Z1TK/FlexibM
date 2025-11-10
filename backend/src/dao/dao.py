from backend.src.dao.base_dao import BaseDAO
from backend.src.author.model import Author

class AuthorDAO(BaseDAO):
    model = Author