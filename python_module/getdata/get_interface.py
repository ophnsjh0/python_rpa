import paramiko
import requests
import json
import time
from json.decoder import JSONDecoder

class GetInterface:
    def __init__(self, switch, session):
        self.switch = switch
        self.session = session
        self.session.verify = False
        self.nodes = ["1101", "1102", "1201"]
         
    def aci(self, token):
        interfaces_data = []
        for node in self.nodes:
            requests.pakages.urllib3.disable_warnings()
            self.session.headers.update(token)
            url = f'https://{self.switch["ip"]}/api/node/class/topology/pod-1/node-{node}/ethpmPhysIf.json'
            response = self.session.get(url)
            if response.status_code == 200:
                interfaces = response.json()['imdata']
                print(f"{node} get interface : ok")
                interfaces_data.append(interfaces)
            else:
                print(f"{node} get interface : Failed")
                exit()
        return interfaces_data
    
    def citrix(self, token):
        requests.pakages.urllib3.disable_warnings()
        self.session.headers.update(token)
        url = f'https://{self.switch["ip"]}/nitro/v1/stat/interface'
        response = self.session.get(url)
        if response.status_code == 200:
            interface_data = response.json()['Interface']
            print(f"{self.switch['name']} Get Interface : ok")
            return interface_data
        else:
            print(f"{self.switch['name']} Get Interface : Failed")
            return None
    
    def cisco(self, ssh_client):
        commands = ["show interface status"]
        if ssh_client:
            stdin, stdout, stderr = ssh_client.exec_command(commands)
            time.sleep(1)
            interface_data = stdout.read().decode('utf-8')
            print(f"{self.switch['name']} Get Interface : ok")
            ssh_client.close()
            return interface_data
        else:
            print(f"{self.switch['name']} Get Interface : Failed")
            return None