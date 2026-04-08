from database import DatabaseManager


class UserService:

    def __init__(self, db):
        self.db = db


    def create_user(self, name, email, role):
        query = "INSERT INTO users (name, email, role) VALUES (?, ?, ?)"
        self.db.cursor.execute(query, (name, email, role))
        self.db.conn.commit()


    def get_users(self):
        query = "SELECT * FROM users"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()


    def update_user(self, user_id, name):
        query = "UPDATE users SET name=? WHERE id=?"
        self.db.cursor.execute(query, (name, user_id))
        self.db.conn.commit()


    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id=?"
        self.db.cursor.execute(query, (user_id,))
        self.db.conn.commit()