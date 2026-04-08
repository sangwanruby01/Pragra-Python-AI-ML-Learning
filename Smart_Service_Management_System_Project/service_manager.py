from database import DatabaseManager

class ServiceManager:

    def __init__(self, db):
        self.db = db


    def add_service(self, service_name, price):
        query = "INSERT INTO services (service_name, price) VALUES (?, ?)"
        self.db.cursor.execute(query, (service_name, price))
        self.db.conn.commit()


    def list_services(self):
        query = "SELECT * FROM services"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()