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
        
    def cisco(self, ssh_client):
        commands = ["show interface status"]
        if ssh_client:
            for command in commands:
                stdin, stdout, stderr = ssh_client.exec_command(command)
                time.sleep(1)
                interface_data = stdout.read().decode('utf-8')
                print(interface_data)
                return interface_data
        else:
            print("failed: Not ssh_client")
            return None
        
    def aci(self, token):
        interfaces_data = []
        for node in self.nodes:
            print(node)
            requests.pakages.urllib3.disable_warnings()
            self.session.headers.update(token)
            url = f'https://{self.switch["ip"]/api/node/class/topology/pod-1/node-{node}/ethpmPhysIf.json}'
            response = self.session.get(url)
            if response.status_code == 200:
                interfaces = response.json()['imdata']
                print(f"{node} get interface : ok")
                interfaces_data.append(interfaces)
            else:
                exit()
        return interfaces_data