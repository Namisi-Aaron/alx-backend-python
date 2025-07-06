#!/usr/bin/python3
import mysql.connector
from .seed import connect_to_prodev

def stream_users():
    """Yields rows one by one from the specified table."""
    table_name = 'user_data'
    
    try:
        connection = connect_to_prodev()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(f"SELECT * FROM {table_name}")
        while True:
            row = cursor.fetchone()
            if row is None:
                break
            yield row

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
