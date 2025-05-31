# FastAPI Form Application

A simple FastAPI application that collects user information through a form and stores it in a JSON file.

## Setup Instructions

### Running Locally

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   cd c:\vscode\Ops
   uvicorn app.main:app --reload
   ```

3. Open your browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

### Using Docker

1. Build the Docker image:
   ```
   docker build -t fastapi-form-app .
   ```

2. Run the Docker container:
   ```
   docker run -d -p 8000:8000 fastapi-form-app    
   ```

3. Open your browser and go to:
   ```
   http://localhost:8000/
   ```

## Features

- Form to collect Name, Email, Phone, and Location
- Data is stored in a JSON file with date and time as identifiers
- View all submissions in a tabular format via web interface
- Clean code organization with separated data handling module
- Docker support for easy deployment
- Responsive UI with form validation
