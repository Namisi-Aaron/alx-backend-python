#!/usr/bin/python3
import csv
import mysql.connector

database_name = 'ALX_prodev'
table_name = 'user_data'
data = 'user_data.csv'

def connect_db():
    """ Connects to mysql database server"""
    try:
        return mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password"
        )
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
        return None


def create_database(connection):
    """Creates the database if it does not exist."""
    if connection:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        connection.close()


def connect_to_prodev():
    """Connects to MySQL database."""
    try:
        return mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database=database_name
        )
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
        return None


def create_table(connection):
    """Creates the user_data table."""
    if connection:
        create_table_script = f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            user_id VARCHAR(36) NOT NULL,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age TINYINT UNSIGNED NOT NULL,
            PRIMARY KEY (user_id),
            INDEX idx_user_id (user_id)
        );
        '''
        with connection.cursor() as cursor:
            cursor.execute(create_table_script)
        connection.close()


def insert_data(connection, data):
    """Insert data using a generator."""
    if connection:
        insert_query = f'''
        INSERT INTO {table_name} (user_id, name, email, age)
        VALUES (%s, %s, %s, %s)
        '''
        with open(data, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            with connection.cursor() as cursor:
                for row in reader:
                    cursor.execute(insert_query, (
                        row['user_id'],
                        row['name'],
                        row['email'],
                        int(row['age'])))
        
        connection.commit()
        connection.close()

if __name__ != '__main__':
    connection = connect_db()
    create_database(connection)
    connect_to_prodev()
    create_table(connection)
    insert_data(connection, data)
