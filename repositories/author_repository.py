from db.run_sql import run_sql
from models.author import Author

# CREATE
def save(author: Author):
    sql = "INSERT into authors (first_name,last_name) VALUES (%s,%s) RETURNING id"
    values = [author.first_name, author.last_name]
    results = run_sql(sql, values)
    if results:
        author.id = results[0]["id"]
    return author


# SHOW
def select_all():
    authors = []
    sql = "SELECT * FROM authors"
    results = run_sql(sql)
    for row in results:
        author = Author(row["first_name"], row["last_name"], row["id"])
        authors.append(author)
    return authors


def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        row = results[0]
        author = Author(row["first_name"], row["last_name"], row["id"])

    return author


# DELETE
def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)
