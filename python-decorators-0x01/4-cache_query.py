import os
import re
import time
import sqlite3 
import functools
from sqlite3 import Error

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'my_database.db')

query_cache = {}

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

def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, query):
        key = (query,)
        if key in query_cache:
            print(f"Cached result:{query_cache[key]}")
            return query_cache[key]
        else:
            result = func(conn, query)
            query_cache[key] = result
            print(f"Result from database: {result}")
            return result
        
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")