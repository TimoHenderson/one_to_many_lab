from repositories import author_repository, book_repository
from models.author import Author
from models.book import Book


def print_authors():
    [print(author) for author in author_repository.select_all()]


def print_books():
    [print(book) for book in book_repository.select_all()]


book_repository.delete_all()
author_repository.delete_all()

author1 = Author("David", "Sonnenschein")
author1 = author_repository.save(author1)

author2 = Author("H.G.", "Wells")
author2 = author_repository.save(author2)


book1 = Book("Sound Design", "Audio", author1)
book1 = book_repository.save(book1)

book2 = Book("The Time Machine", "Sci-Fi", author2)
book2 = book_repository.save(book2)

print_authors()
print_books()
