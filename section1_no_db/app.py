"""
list of books, initial values
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


app = Flask(__name__)

books_list = [
    {
        "id": 0,
        "author": "Zika",
        "language": "russian",
        "title": "Zikisimo",
    },
    {
        "id": 1,
        "author": "Vlada Arsic",
        "language": "serbian",
        "title": "Kad zvona zaneme",
    },
    {
        "id": 2,
        "author": "Slobodan Stojanovic",
        "language": "serbian",
        "title": "Nesto lepo",
    },
    {
        "id": 3,
        "author": "Tolkin",
        "language": "english",
        "title": "Lord of the rings",
    }
]

#books_list = []


@app.route("/books", methods=["GET", "POST"])
def books():
    if request.method == "GET":
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            return "No books available."

    if request.method == "POST":
        new_id = books_list[-1]["id"] + 1
        new_author = request.form["author"]
        new_language = request.form["language"]
        new_title = request.form["title"]

        new_book = {
                "id": new_id,
                "author": new_author,
                "language": new_language,
                "title": new_title,
                }

        books_list.append(new_book)

        return f"Book with id: {new_id}, title: {new_title} has been added successfully."


@app.route("/book/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_book(id):
    if request.method == "GET":
        try:
            book = [book for book in books_list if book["id"] == id][0]
            return jsonify(book)
        except:
            return f"Book with id {id} does not exist"

    if request.method == "PUT":
        try:
            book = [book for book in books_list if book["id"] == id][0]

            book["author"] = request.form["author"]
            book["language"] = request.form["language"]
            book["title"] = request.form["title"]
            return f"Book with id {id} has been updated."
        except:
            return f"Book with id {id} does not exist."

    if request.method == "DELETE":
        try:
            book = [book for book in books_list if book["id"] == id][0]
            books_list.remove(book)
            return f"Book with id {id} has been deleted."
        except:
            return f"Book with id {id} does not exist."


if __name__ == "__main__":
    app.run(debug=True)
