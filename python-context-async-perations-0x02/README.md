## Advanced Python: Generators, Decorators, Context Managers, and Asynchronous Programming

This directory contais files for alx project *Advanced Python: Generators, Decorators, Context Managers, and Asynchronous Programming*
 - **0-databaseconnection.py** - contains a class based context manager that handles opening and closing database connections automatically
 - **1-execute.py** - contains a reusable context manager that takes a query (and optional parameters) as input and executes it. It also manages both connection and the query execution
 - **3-concurrent.py** - contains a file that runs multiple database queries concurrently using asyncio.gather().

All these files utilize a sqlite database located at the root of this directory named *my_database.db*
Create this file and seed it with user data with columns **id**, **name**, **email** and **age** in a **users** table to test the code in this directory.