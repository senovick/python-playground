import sqlite3


class Db:
    def __init__(self):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)"
        )
        self.conn.commit()
        self.conn.close()

    def connect(self):
        try:
            self.conn = sqlite3.connect("books.db")
            self.cur = self.conn.cursor()
            print("Database Connected!")
        except sqlite3.DatabaseError as e:
            print("Problem Connecting to the Database")
            print(e)
            self.conn.close()

    def insert(self, title, author, year, isbn):
        try:
            self.cur.execute(
                "INSERT INTO bookstore VALUES(NULL,?,?,?,?)",
                (title, author, year, isbn),
            )
            self.conn.commit()
            # get last record inserted
            self.cur.execute("SELECT * FROM bookstore ORDER BY id DESC LIMIT 1")
            result = self.cur.fetchall()
        except sqlite3.DataError as e:
            print("There was a problem inserting the data")
            print(e)
        finally:
            self.conn.close()
            return result

    def get_books(self):
        self.cur.execute("SELECT * from bookstore")
        result = self.cur.fetchall()
        self.conn.close()
        print("Database Closed!")
        return result

    def get_book(self, id):
        self.cur.execute("SELECT * FROM bookstore WHERE id=?", (id,))
        result = self.cur.fetchall()
        return result

    def search(self, title="", author="", year="", isbn=""):
        try:
            self.cur.execute(
                "SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=?",
                (title, author, year, isbn),
            )
            result = self.cur.fetchall()
            if len(result) == 0:
                result = "Book not found"
        except sqlite3.Error as e:
            result = "Error getting books"
        finally:
            self.conn.close()
        return result

    def update(self, title, author, year, isbn, id):
        try:
            self.cur.execute(
                "UPDATE bookstore SET title=?, author=?, year=?, isbn=? WHERE id=?",
                (title, author, year, isbn, id),
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error Updating Book " + e)
        finally:
            self.conn.close()

    def delete(self, id):
        try:
            self.cur.execute("DELETE FROM bookstore WHERE id=?", (id,))
            self.conn.commit()
            print("Book was successfully deleted!")
        except sqlite3.Error as e:
            print("An error occured deleting the book - {}".format(e))
        finally:
            self.conn.close()
