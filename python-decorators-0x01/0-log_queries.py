import os
import sqlite3
import functools
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'my_database.db')

def log_queries(func):
    def wrapper(query):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{query}] ran at [{timestamp}]")
        return func(query)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
print(users)