from db.run_sql import run_sql
from models.book import Book
from repositories import author_repository

# CREATE
def save(book: Book):
    sql = "INSERT into books(title,genre,author_id) VALUES (%s,%s,%s) RETURNING id"
    values = [book.title, book.genre, book.author.id]
    results = run_sql(sql, values)
    if results:
        book.id = results[0]["id"]
    return book


# SHOW
def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    for row in results:
        author = author_repository.select(row["author_id"])
        book = Book(row["title"], row["genre"], author, row["id"])
        books.append(book)
    return books


# SHOW
def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
        author = author_repository.select(row["author_id"])
        book = Book(row["title"], row["genre"], author, row["id"])
    return book


def update(book):
    sql = "UPDATE books SET (title,genre,author_id) = (%s,%s,%s) WHERE id = %s"
    values = [book.title, book.genre, book.author.id, book.id]
    run_sql(sql, values)


# DELETE
def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)
