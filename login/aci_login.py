import requests
import json
from json.decoder import JSONDecoder

class Aci_Login:
    def __init__(self, switch):
        self.switch = switch
        
    session = requests.Session()
    session.verify = False
    session.headers.update({'Content-Type': 'application/json'})
    
    def login_aci(self):
        url = f'https://{switch["ip"]}/api/aaaLogin.json'
        login = {
            "aaaUser": {
                "attributes": {
                    "name": f"{switch['id']}",
                    "pwd" : f"{switch['password']}",
                }
            }
        }
        response = session.post(url, json=login)
        if response.status.code == 200:
            print("Login successful")
        else:
            print(f"Login failed: {response.text}")
            print(response.status.code)
            exit()