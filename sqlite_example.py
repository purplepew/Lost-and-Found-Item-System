import sqlite3 

def populateDb():
    with sqlite3.connect("./lib/data.db") as conn:
        cursor = conn.cursor()
        
        # Creates users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)

        # Creates items table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                type TEXT CHECK(type IN ('LOST', 'FOUND')),
                status TEXT DEFAULT 'OPEN',
                category TEXT,
                description TEXT,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)

        # --- ADD DUMMY DATA ---

        # Check if users table is already seeded
        cursor.execute("SELECT COUNT(*) FROM users")
        if cursor.fetchone()[0] > 0:
            print("Database already seeded. Skipping.")
            return

        # 1. Dummy Users
        dummy_users = [
            ('Alice Smith', 'alice@example.com'),
            ('Bob Johnson', 'bob@example.com'),
            ('Charlie Brown', 'charlie@example.com')
        ]
        cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", dummy_users)
        print(f"Added {len(dummy_users)} users.")

        # 2. Dummy Items (using user_ids 1, 2, 3 for Alice, Bob, Charlie)
        dummy_items = [
            # Items belonging to Alice (user_id = 1)
            (1, 'LOST', 'Electronics', 'Lost my black Sony headphones near the park.'),
            (1, 'FOUND', 'Keys', 'Found a set of Toyota car keys.'),
            
            # Items belonging to Bob (user_id = 2)
            (2, 'LOST', 'Book', 'Left my "Python Crash Course" book on the bus.'),
            
            # Items belonging to Charlie (user_id = 3)
            (3, 'FOUND', 'Pet', 'Found a small brown dog with a red collar.'),
            (3, 'LOST', 'Apparel', 'Lost a blue North Face jacket at the coffee shop.')
        ]
        cursor.executemany("""
            INSERT INTO items (user_id, type, category, description) 
            VALUES (?, ?, ?, ?)
        """, dummy_items)
        print(f"Added {len(dummy_items)} items.")

        # Save the changes to the database
        conn.commit()
        print("Database seeding complete.")

