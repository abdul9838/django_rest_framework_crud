import requests
import json

URL = 'http://127.0.0.1:8000/studentapi/'

def get_data(id=None):
    data = {}
    if id is not None:
        data = {"id" : id}
        
    json_data = json.dumps(data)
    r = requests.get(url = URL , data = json_data)
    data = r.json()
    print(data)

get_data()

def post_data():
    data = {
        "name": "Rahul",
        "roll": 105,
        "city": "Dhanbaddd"
    }
    response = requests.post(url=URL, json=data) 
    
    print(response.json()) if response.status_code == 200 else print(f"Failed to send POST request: {response.status_code}")

post_data()
def update_data():
    data = {
        'id':5,
        "name": "Raaahul",
        "city": "Dhanbd"
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL,data=json_data)
    data = r.json()
    print(data)

update_data()

def delete_data():
    data = {'id': 2}
    json_data = json.dumps(data)
    r = requests.delete(url=URL,data = json_data)
    print(r.status_code)
    if r.status_code == 200:  
        print("Data deleted successfully")
    else:
        print("Failed to delete data")

delete_data()