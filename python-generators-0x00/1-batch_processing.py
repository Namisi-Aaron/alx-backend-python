#!/usr/bin/python3
from .seed import connect_to_prodev

def stream_users_in_batches(batch_size):
    """Alternative version using context manager"""
    connection = connect_to_prodev()
    
    cursor = connection.cursor(dictionary=True)
    try:
        query = "SELECT * FROM user_data"
        cursor.execute(query)
        while True:
            batches = cursor.fetchmany(batch_size)
            if batches:
                yield batches
            else:
                break
    finally:
        cursor.close()
        connection.close()

def batch_processing(batch_size):
    """
    Generator that yields batches of users in specified size.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] >= 25:
                yield user
