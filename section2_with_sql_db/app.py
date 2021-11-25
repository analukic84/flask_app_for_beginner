"""
connect to sql database
dictionary format: id, author, language, title

create Flask app
/books - list of all books - GET
/books - add a new book to the books - POST

CRUD
/book/id - get the book - GET
/book/id - update the book - PUT
/book/id - delete the book - DELETE
"""

from flask import Flask, request, jsonify
from section2_with_sql_db.utils import database


app = Flask(__name__)

database.create_book_table()


@app.route("/books", methods=["GET", "POST"])
def books():
    if request.method == "GET":
        books = database.get_all_books()
        if len(books) > 0:
            return jsonify(books)
        else:
            return "No books available."

    if request.method == "POST":
        new_author = request.form["author"]
        new_language = request.form["language"]
        new_title = request.form["title"]

        database.add_book(new_author, new_language, new_title)

        return f"Book title: {new_title} has been added successfully."


@app.route("/book/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_book(id):
    if request.method == "GET":
        book = database.get_book_by_id(id)

        if book:
            return jsonify(book)
        else:
            return f"Book with id {id} does not exist"

    if request.method == "PUT":
        new_author = request.form["author"]
        new_language = request.form["language"]
        new_title = request.form["title"]

        book = database.get_book_by_id(id)
        if book:
            database.update_book_by_id(id, new_author, new_language, new_title)
            return f"Book id {id}, title {new_title} has been updated successfully."
        else:
            return f"Book with id {id} does not exist"

    if request.method == "DELETE":
        book = database.get_book_by_id(id)
        if book:
            database.delete_book_by_id(id)
            return f"Book id {id} has been deleted successfully."
        else:
            return f"Book with id {id} does not exist"


if __name__ == "__main__":
    app.run(debug=True)
