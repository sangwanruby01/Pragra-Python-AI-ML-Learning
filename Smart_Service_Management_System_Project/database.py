import sqlite3

class DatabaseManager:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        # Users table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            role TEXT
        )
        """)

        # Services table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS services (
            service_id INTEGER PRIMARY KEY AUTOINCREMENT,
            service_name TEXT NOT NULL,
            price REAL NOT NULL
        )
        """)

        # Bookings table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            service_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(service_id) REFERENCES services(service_id)
        )
        """)

        self.conn.commit()

    def close(self):
        self.conn.close()