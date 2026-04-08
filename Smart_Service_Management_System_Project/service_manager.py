from database import DatabaseManager # Import the DatabaseManager class

class ServiceManager:

    def __init__(self, db):
        self.db = db


    def add_service(self, service_name, price):   # Method to add a new service to the services table
        query = "INSERT INTO services (service_name, price) VALUES (?, ?)"
        self.db.cursor.execute(query, (service_name, price))
        self.db.conn.commit()


    def list_services(self):   # Method to retrieve all services from the database
        query = "SELECT * FROM services"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()