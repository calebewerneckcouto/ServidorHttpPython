# Event Management API

## Description
This project provides a simple Event Management API implemented using Flask and an HTTP server. It allows you to manage events by performing operations such as listing, creating, updating, and deleting events. Events can be either in-person or online.

## Features
- List all events
- Retrieve an event by ID
- Create new events (online or in-person)
- Update existing events (fully or partially)
- Delete events
- Serve event data via a web interface or REST API

## Technologies Used
- Python
- Flask
- HTTP Server (`http.server` module)

## How to Run

### Prerequisites
- Python 3.8 or higher
- Flask installed (`pip install flask`)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/event-management-api.git
   cd event-management-api
pip install -r requirements.txt
python app.py
Access the API at:

Root: http://127.0.0.1:5000/
Event list: http://127.0.0.1:5000/api/eventos/
Retrieve event by ID: http://127.0.0.1:5000/api/eventos/<id>/
Create an event: Send a POST request to /api/eventos/ with JSON payload.
Update an event: Send a PUT or PATCH request to /api/eventos/<id>/.
Delete an event: Send a DELETE request to /api/eventos/<id>/.
Run the standalone HTTP server:

bash
Copy code
python server.py
Access the HTTP server at:

Root: http://localhost:8000/
Event list: http://localhost:8000/eventos
Event API: http://localhost:8000/api/eventos
API Endpoints
Event Endpoints
Method	Endpoint	Description
GET	/api/eventos/	List all events
GET	/api/eventos/<id>/	Get event details by ID
POST	/api/eventos/	Create a new event
PUT	/api/eventos/<id>/	Fully update an event by ID
PATCH	/api/eventos/<id>/	Partially update an event by ID
DELETE	/api/eventos/<id>/	Delete an event by ID
Example Event Object
json
Copy code
{
  "id": 1,
  "nome": "Aula de Python",
  "local": "Rio de Janeiro"
}
Contribution
Feel free to fork this repository and submit pull requests for new features or bug fixes.
