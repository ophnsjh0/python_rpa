import paramiko
import requests
import json
import time
from json.decoder import JSONDecoder
from datetime import datetime


class GetPower:
    def __init__(self, switch, session):
        self.switch = switch
        self.session = session
        self.session.verify = False
        self.nodes = ['1101']
        
    def aci(self, token):
        requests.pakages.urllib3.disable_warnings()
        self.session.headers.update(token)
        url = f'https://{self.switch["ip"]}/api/node/class/eqptPsu.json'
        response = self.session.get(url)
        if response.status.code == 200:
            power_data = response.json()['imdata']
            print(f"ACI get Power : ok")
        else:
            print(f"ACI get Power : Failed")
            exit()
        return power_data
    
    def cisco(self, ssh_client):
        commands = [f"show env power"]
        if ssh_client:
            stdin, stdout, stderr = ssh_client.exec_command(commands)
            time.sleep(1)
            power_data = stdout.read().decode('utf-8')
            print(f"{self.switch['name']} get Power : ok")
            ssh_client.close()
            return power_data
        else:
            print(f"{self.switch['name']} get Power : Failed")
            return None