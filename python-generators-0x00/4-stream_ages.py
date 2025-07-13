#!/usr/bin/python3
seed = __import__('seed')

def stream_user_ages():
    '''
    Fetches and yields user ages from the database.
    '''
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row['age']
    connection.close()

def calculate_average_age():
    '''
    Calculates and returns the average age of all users.
    '''
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    print(f"Average age of users: {total_age / count}")
    return total_age / count