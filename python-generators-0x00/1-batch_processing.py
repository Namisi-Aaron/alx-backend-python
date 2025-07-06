#!/usr/bin/python3
from .seed import connect_db

def stream_users_in_batches(batch_size):
    """Alternative version using context manager"""
    table_name = 'users'
    connection = connect_db()
    
    cursor = connection.cursor(dictionary=True)
    try:
        query = f'''
        SELECT * FROM {table_name};
        '''
        cursor.execute(query)
        while True:
            rows = cursor.fetchmany(batch_size)
            if rows:
                yield rows
            else:
                break
    finally:
        cursor.close()

def batch_processing(batch_size):
    """
    Generator that yields batches of users in specified size.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] >= 25:
                yield user

