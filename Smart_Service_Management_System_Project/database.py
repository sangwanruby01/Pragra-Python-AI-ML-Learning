import sqlite3  # Import the sqlite3 library

class DatabaseManager:   # DatabaseManager class
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):    # Method to establish a connection to the SQLite database
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):   # Method to create required tables if they do not already exist

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

        self.conn.commit()   # Save all changes to the database

    def close(self):
        self.conn.close() # Close the connection to the database