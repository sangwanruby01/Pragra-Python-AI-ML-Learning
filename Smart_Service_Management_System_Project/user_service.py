from database import DatabaseManager # Import the DatabaseManager class

class UserService:

    def __init__(self, db):
        self.db = db


    def create_user(self, name, email, role):  # Method to create a new user in the users table
        query = "INSERT INTO users (name, email, role) VALUES (?, ?, ?)"
        self.db.cursor.execute(query, (name, email, role))
        self.db.conn.commit()


    def get_users(self):   # Method to retrieve all users from the database
        query = "SELECT * FROM users"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()


    def update_user(self, user_id, name):  # Method to update a user's name using their user ID
        query = "UPDATE users SET name=? WHERE id=?"
        self.db.cursor.execute(query, (name, user_id))
        self.db.conn.commit()


    def delete_user(self, user_id):     # Method to delete a user from the database using their user ID
        query = "DELETE FROM users WHERE id=?"
        self.db.cursor.execute(query, (user_id,))
        self.db.conn.commit()