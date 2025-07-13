#!/usr/bin/python3
seed = __import__('seed')

def stream_users_in_batches(batch_size):
    """Alternative version using context manager"""
    connection = seed.connect_to_prodev()
    
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
    users_list = []

    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] >= 25:
                users_list.append(user)
        
        return users_list
