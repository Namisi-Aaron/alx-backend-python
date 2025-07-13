import sqlite3
import os
from sqlite3 import Error

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'my_database.db')


def with_db_connection(func):
    '''
    Automatically connects to the SQLite database
    and closes it after the function execution.
    '''
    def wrapper(*args, **kwargs):
        conn = None
        try:
            conn = sqlite3.connect(db_path)
            print(f"Successfully connected to database: {db_path}")
            result = func(conn, *args, **kwargs)
            return result
        except Error as e:
            print(f"Error connecting to database: {e}")
        finally:
            if conn:
                conn.close()
                print(f"Connection closed")
    return wrapper

@with_db_connection 
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id =?", (user_id,))
    return cursor.fetchone()

user = get_user_by_id(user_id=1)
print(user)
