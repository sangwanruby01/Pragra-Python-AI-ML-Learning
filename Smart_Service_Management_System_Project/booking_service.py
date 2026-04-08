# Import the DatabaseManager class from the database module

from database import DatabaseManager

class BookingManager:   # BookingManager class


    def __init__(self, db):   #Method that receives the database object
        self.db = db


    def create_booking(self, user_id, service_id, date):  # Method to create a new booking
        query = "INSERT INTO bookings (user_id, service_id, date) VALUES (?, ?, ?)"
        self.db.cursor.execute(query, (user_id, service_id, date)) # Execute the query
        self.db.conn.commit()  # Commit the transaction to save the changes permanently


    def get_user_bookings(self, user_id):  # Method to retrieve all bookings
        query = "SELECT * FROM bookings WHERE user_id=?"
        self.db.cursor.execute(query, (user_id,))  # Execute the query
        return self.db.cursor.fetchall() # Fetch and return all matching booking records