import sqlite3

# Step 1: Connect to the database or create it if it doesn't exist
conn = sqlite3.connect('app.db')

# Step 2: Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Step 3: Create a table in the database
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT
    )
''')

# Step 4: Insert data into the table
user_data = [
    (1, 'user1', 'user1@example.com'),
    (2, 'user2', 'user2@example.com'),
    (3, 'user3', 'user3@example.com'),
    (4, 'sample1', 'sample1@example.com'),
    (5, 'sample2', 'sample2@example.com'),
    (6, 'hello1', 'hello1@example.com'),
    (7, 'hello2', 'hello2@example.com'),
    (8, 'panda1', 'panda1@example.com'),
    (9, 'apple1', 'apple1@example.com'),
    (10, 'apple2', 'apple2@example.com')
]

cursor.executemany('INSERT INTO users (id, username, email) VALUES (?, ?, ?)', user_data)

# Step 5: Commit the changes and close the connection
conn.commit()
conn.close()