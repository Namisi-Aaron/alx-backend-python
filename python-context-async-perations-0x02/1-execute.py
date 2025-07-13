import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'my_database.db')

class ExecuteQuery:
    """
    Manages opening and closing the connection.
    It also implements a context manager for executing queries
    with optional parameters.
    """
    def __init__(self, db_path: str, query: str, params=()):
        self.db_path = db_path
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        
        return self.cursor.execute(self.query, self.params)

    def __exit__(self, exc_type, exc_val, traceback):
        if self.connection:
            if exc_type is None:
                self.connection.commit()
            else:
                self.connection.rollback()
                print(f"Rolling back transaction due to error: {exc_val}")
            self.connection.close()
        
        self.connection = None
        self.cursor = None

select_query = "SELECT * FROM users WHERE age > ?"
params = (25,)

with ExecuteQuery(db_path, select_query, params) as e:
    users = e.fetchall()
    for user in users:
        print(f"{user}")