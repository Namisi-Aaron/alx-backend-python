import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'my_database.db')

class DatabaseConnection:
    '''
    Automatically connects to the SQLite database
    and closes it after query execution.
    '''
    def __init__(self, db_path):
        self.db_path = db_path
    
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        return self.connection
    
    def __exit__(self, exc_type, exc_val, traceback):
        self.connection.close()

with DatabaseConnection(db_path) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()

    print("Users:", users)
