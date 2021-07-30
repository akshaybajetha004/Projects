import sqlite3


class Database:
    def __init__(self, query):
        self.query = query

    def create_connection(self):

        try:
            self.conn = sqlite3.connect('stackoverflow.db', timeout=10)

        except sqlite3.Error as error:
            print(f"Problem in connection: {error}")

        c = self.conn.cursor()
        return c

    def close_connection(self):

        return self.conn.close()

    def execute(self):

        c = self.create_connection()
        c.execute("PRAGMA foreign_keys=ON")

        try:
            if type(self.query) == tuple:
                c.execute(*self.query)
            else:
                c.execute(self.query)
            self.conn.commit()

        except sqlite3.Error as error:
            print(f"Problem in executing query: {error}")

        finally:
            self.close_connection()


