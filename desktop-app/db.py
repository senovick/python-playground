import sqlite3


class Db:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = sqlite3.connect("books.db")
            self.cur = self.conn.cursor()
            self.cur.execute(
                "CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)"
            )
            self.conn.commit()
            print("DATABASE CONNECTED")
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
            print("data successfully inserted!")
        except sqlite3.DataError as e:
            print("There was a problem inserting the data")
            print(e)
        finally:
            self.conn.close()

    def get_books(self):
        self.cur.execute("SELECT * from bookstore")
        result = self.cur.fetchall()
        return result
