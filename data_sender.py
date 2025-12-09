import requests

url = "http://localhost:8000"

data = [
    {
        "name": "Nandu",
        "email": "dinwiz2@gmom.c",
        "phone": "1234567890",
        "location": "India"
    },
    {
        "name": "Alice",
        "email": "dwb@f.c",
        "phone": "0987654321",
        "location": "USA"
    },
    {
        "name": "Bob",
        "email": "dwin@fe.c",
        "phone": "1122334455",  
        "location": "UK"
    }
]

for entry in data:
    response = requests.post(f"{url}/submit", data=entry)
    print(f"Submitted: {entry['name']}, Status Code: {response.status_code}")