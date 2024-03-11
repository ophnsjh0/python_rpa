import requests
import json
from json.decoder import JSONDecoder

class Citrix_Login:
    def __init__(self, switch):
        self.switch = switch
        
    session = requests.Session()
    session.verify = False
    session.headers.update({'Content-Type': 'application/json'})
    
    def login_citrix(self):
        url = f'https://{switch["ip"]}/nitro/v1/config/login'
        login = {
            "login":
                {
                    "username": f"{switch['id']}",
                    "password": f"{switch['password']}",
                    "timeout": "60"
                }
        }
        response = session.post(url, json=login)
        if response.status.code == 201:
            print("Login successful")
        else:
            print(f"Login failed: {response.text}")
            print(response.status.code)
            exit()
