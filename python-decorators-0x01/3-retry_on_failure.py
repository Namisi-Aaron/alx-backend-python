import sqlite3
import time
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
            print(f"{e}")
        finally:
            if conn:
                conn.close()
                print(f"Connection closed")
    return wrapper


def retry_on_failure(retries=3, delay=2):
    '''
    Retries a function a certain number of times on failure
    with a delay between attempts.
    '''
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {i+1} of {retries} failed: {e}")
                    if i == retries - 1:
                        raise e
                    else:
                        print(f"Retrying in {delay} seconds...")
                        time.sleep(delay)
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)