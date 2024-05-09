import paramiko
import requests
import json
import time
from json.decoder import JSONDecoder

class GetMem:
    def __init__(self, switch, session):
        self.switch = switch
        self.session = session
        self.session.verify = False
        self.nodes = ["1101", "1102", "1201"]
               
    def aci(self, token):
        mem_data = []
        for node in self.nodes:
            requests.pakages.urllib3.disable_warnings()
            self.session.headers.update(token)
            url = f'https://{self.switch["ip"]}/api/node/mo/topology/pod-1/node-{node}/sys/procsys/HDprocSysMem5min-0.json'
            response = self.session.get(url)
            if response.status_code == 200:
                mem = response.json()['imdata']
                print(f"{node} get MEM : ok")
                mem_data.append(mem)
            else:
                print(f"{node} get MEM : Failed")
                exit()
        return mem_data
    
    def citrix(self, token):
        requests.pakages.urllib3.disable_warnings()
        self.session.headers.update(token)
        url = f'https://{self.switch["ip"]}/nitro/v1/stat/ns'
        response = self.session.get(url)
        if response.status_code == 200:
            mem_data = response.json()['ns']
            print(f"{self.switch['name']} Get MEM : ok")
            return mem_data
        else:
            print(f"{self.switch['name']} Get MEM : Failed")
            return None
    
    def cisco(self, ssh_client):
        commands = ["show memory summary | include Processor"]
        if ssh_client:
            stdin, stdout, stderr = ssh_client.exec_command(commands)
            time.sleep(1)
            mem_data = stdout.read().decode('utf-8')
            print(f"{self.switch['name']} Get MEM : ok")
            ssh_client.close()
            return mem_data
        else:
            print(f"{self.switch['name']} Get MEM : Failed")
            return None