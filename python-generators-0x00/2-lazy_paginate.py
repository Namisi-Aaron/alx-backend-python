#!/usr/bin/python3
seed = __import__('seed')

def paginate_users(page_size, offset):
    '''
    Fetches a page of users from the database.
    '''
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_paginate(page_size):
    '''
    Generates a lazy iterator for paginated user data.
    '''
    offset = 0
    while True:
        users_page = paginate_users(page_size, offset)
        if not users_page:
            break
        yield users_page
        offset += page_size