import requests

url = "http://localhost:8000/submissions/json"


for _ in range(10):
    response = requests.get(url)
    if response.status_code == 200:
        submissions = response.json()
        print(submissions)
    else:
        print(f"Failed to retrieve submissions: {response.status_code}")