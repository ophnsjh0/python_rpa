import paramiko
import requests
import json
import time
from json.decoder import JSONDecoder
from datetime import datetime

class GetFan:
    def __init__(self, switch, session):
        self.switch = switch
        self.session = session
        self.session.verify = False
        self.nodes = ["1101", "1102", "1201"]
        
 
        
    def aci(self, token):
        requests.pakages.urllib3.disable_warnings()
        self.session.headers.update(token)
        url = f'https://{self.switch["ip"]}/api/node/class/eqptFt.json'
        response = self.session.get(url)
        if response.status_code == 200:
            fan_data = response.json()['imdata']
            print(f"ACI get Fan : ok")
        else:
            print(f"ACI get Fan :  Failed")
            exit()
        return fan_data
    
    def cisco(self, ssh_client):
        commands = ["show env fan"]
        if ssh_client:
            stdin, stdout, stderr = ssh_client.exec_command(commands)
            time.sleep(1)
            fan_data = stdout.read().decode('utf-8')
            print(f"{self.switch['name']} Get FAN : ok")
            ssh_client.close()
            return fan_data
        else:
            print(f"{self.switch['name']} Get FAN : Failed")
            return None
        
    # def citrix(self, token):
    #     requests.pakages.urllib3.disable_warnings()
    #     self.session.headers.update(token)
    #     url = f'https://{self.switch["ip"]}/nitro/v1/stat/system'
    #     response = self.session.get(url)
    #     if response.status_code == 200:
    #         cpu_data = response.json()['system']
    #         print(f"{self.switch['name']} Get GPU : ok")
    #         return cpu_data
    #     else:
    #         print(f"{self.switch['name']} Get CPU : Failed")
    #         return None