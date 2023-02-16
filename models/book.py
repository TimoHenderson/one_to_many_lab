from dataclasses import dataclass
from models.author import Author


@dataclass
class Book:
    title: str
    genre: str
    author: Author
    id: int = None
