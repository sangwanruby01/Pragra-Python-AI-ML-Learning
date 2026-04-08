from database import DatabaseManager

class BookingManager:

    def __init__(self, db):
        self.db = db


    def create_booking(self, user_id, service_id, date):
        query = "INSERT INTO bookings (user_id, service_id, date) VALUES (?, ?, ?)"
        self.db.cursor.execute(query, (user_id, service_id, date))
        self.db.conn.commit()


    def get_user_bookings(self, user_id):
        query = "SELECT * FROM bookings WHERE user_id=?"
        self.db.cursor.execute(query, (user_id,))
        return self.db.cursor.fetchall()