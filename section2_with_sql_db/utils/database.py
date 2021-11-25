from section2_with_sql_db.utils.database_connection import DatabaseConnection

database_file = "books_file.db"


def create_book_table():
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS books(
                    id integer PRIMARY KEY,
                    author text NOT NULL,
                    language text NOT NULL,
                    title text NOT NULL
                )""")


def get_all_books():
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM books")

        all_books = cursor.fetchall()

        return [book for book in all_books]


def add_book(author, language, title):
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()

        sql_string = """
        INSERT INTO books (author, language, title) VALUES (?, ?, ?)
        """

        cursor.execute(sql_string, (author, language, title, ))


def get_book_by_id(id):
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()

        sql_string = "SELECT * FROM books WHERE id=?"

        cursor.execute(sql_string, (id, ))

        book = cursor.fetchone()

        return book


def update_book_by_id(id, author, language, title):
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()

        sql_string = """UPDATE books SET
                            author=?,
                            language=?,
                            title=?
                        WHERE id=?
                     """

        cursor.execute(sql_string, (author, language, title, id, ))


def delete_book_by_id(id):
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()

        sql_string = "DELETE FROM books WHERE id=?"

        cursor.execute(sql_string, (id, ))
