# Import classes to create a basic HTTP server
from http.server import BaseHTTPRequestHandler, HTTPServer

# Import json module to send and receive JSON data
import json

# Import project modules
from database import DatabaseManager
from user_service import UserService
from service_manager import ServiceManager
from booking_service import BookingManager


db = DatabaseManager()  # Initialize the database manager
db.connect()     # Connect to the SQLite database
db.create_tables()  # Create tables if they do not already exist

# Initialize service classes with database connection
user_service = UserService(db)
service_manager = ServiceManager(db)
booking_manager = BookingManager(db)


class RequestHandler(BaseHTTPRequestHandler):  # Custom request handler class to manage HTTP requests

    def do_GET(self):   # Handle GET requests
        if self.path == "/users":
            response = user_service.get_users()

        elif self.path == "/services":
            response = service_manager.list_services()

        elif self.path == "/bookings":
            response = booking_manager.get_bookings()

        else:
            response = {"message": "Invalid endpoint"}

        self.send_response(200)     # Send HTTP response status code
        self.send_header("Content-Type", "application/json")   # Set response header type as JSON
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):    # Handle POST requests
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)    # Convert JSON data to Python dictionary

        if self.path == "/users":
            response = user_service.create_user(
                data.get("name"),
                data.get("email"),
                data.get("role")
            )

        elif self.path == "/services":
            response = service_manager.add_service(
                data.get("name"),
                data.get("price")
            )

        elif self.path == "/book":
            response = booking_manager.create_booking(
                data.get("user_id"),
                data.get("service_id"),
                data.get("date")
            )

        else:
            response = {"message": "Invalid endpoint"}

        self.send_response(200)    # Send response
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def do_PUT(self):       # Handle PUT requests

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        if self.path == "/users":
            response = user_service.update_user(
                data.get("id"),
                data.get("name")
            )
        else:
            response = {"message": "Invalid endpoint"}

        self.send_response(200)     # Send response
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def do_DELETE(self):       # Handle DELETE requests

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        if self.path == "/users":
            response = user_service.delete_user(
                data.get("id")
            )
        else:
            response = {"message": "Invalid endpoint"}

        self.send_response(200)     # Send response
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


if __name__ == "__main__":     # Main entry point of the program
    server = HTTPServer(("localhost", 8000), RequestHandler)   # Create an HTTP server running on localhost port 8000
    print("Server running on http://localhost:8000")
    server.serve_forever()   # Start the server and keep it running