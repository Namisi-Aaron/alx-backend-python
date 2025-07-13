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

def transactional(func):
    '''
    Wraps a function running a database operation inside a transaction.
    If the function raises an error, rollback;
    otherwise commit the transaction
    '''
    def wrapper(connection, *args, **kwargs):
        try:
            func(connection, *args, **kwargs)
            connection.commit()
        except Error as e:
            print(f"An error occured: {e}")
            connection.rollback()
        print("Transaction committed successfully")
    return wrapper

@with_db_connection 
@transactional
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))

update_user_email(user_id=1, new_email='crawford_cartwright@hotmail.com')