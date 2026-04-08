from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from database import DatabaseManager
from user_service import UserService
from service_manager import ServiceManager
from booking_service import BookingManager


db = DatabaseManager()
db.connect()
db.create_tables()

user_service = UserService(db)
service_manager = ServiceManager(db)
booking_manager = BookingManager(db)


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/users":
            response = user_service.get_users()

        elif self.path == "/services":
            response = service_manager.list_services()

        elif self.path == "/bookings":
            response = booking_manager.get_bookings()

        else:
            response = {"message": "Invalid endpoint"}

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

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

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def do_PUT(self):

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

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def do_DELETE(self):

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        if self.path == "/users":
            response = user_service.delete_user(
                data.get("id")
            )
        else:
            response = {"message": "Invalid endpoint"}

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), RequestHandler)
    print("Server running on http://localhost:8000")
    server.serve_forever()