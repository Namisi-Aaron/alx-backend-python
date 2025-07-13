import os
import asyncio
import aiosqlite

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'my_database.db')

async def fetch_concurrently():
    '''
    Fetches users concurrently using asyncio.gather.
    '''
    async def async_fetch_users():
        '''
        Fetches all users from the database.
        '''
        async with aiosqlite.connect(db_path) as conn:
            cursor = await conn.execute("SELECT * FROM users")
            users = await cursor.fetchall()
            return users

    async def async_fetch_older_users():
        '''
        Fetches users with age greater than 40 from the database.
        '''
        async with aiosqlite.connect(db_path) as conn:
            cursor = await conn.execute("SELECT * FROM users WHERE id > 40")
            users = await cursor.fetchall()
            return users
        
    results = asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

    users, older_users = await results
    print(f"All users: {users}")
    print(f"Older users: {older_users}")

asyncio.run(fetch_concurrently()) 
