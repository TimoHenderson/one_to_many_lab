from flask import render_template, request, Blueprint, redirect
from models.book import Book
from repositories import book_repository, author_repository

books_blueprint = Blueprint("books", __name__)

# INDEX
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", books=books)


# SHOW
@books_blueprint.route("/books/<id>")
def show(id):
    book = book_repository.select(id)
    return render_template("books/show.html", book=book)


# CREATE
@books_blueprint.route("/books/new")
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", authors=authors)


@books_blueprint.route("/books", methods=["POST"])
def create_book():
    form = request.form
    author = author_repository.select(form["author_id"])
    book = Book(form["title"], form["genre"], author)
    book_repository.save(book)
    return redirect("/books")


@books_blueprint.route("/books/<id>/edit")
def edit_book(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template("books/edit.html", authors=authors, book=book)


@books_blueprint.route("/books/<id>", methods=["POST"])
def update_book(id):
    form = request.form
    author = author_repository.select(form["author_id"])
    book = Book(form["title"], form["genre"], author, id)
    book_repository.update(book)
    return redirect("/books")
