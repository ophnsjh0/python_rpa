import paramiko
import requests
import json
import time
from json.decoder import JSONDecoder

class GetGeneral:
    def __init__(self, switch, session):
        self.switch = switch
        self.session = session
        self.session.verify = False
        self.nodes = ["1101", "1102", "1201"]
               
    def aci(self, token):
        general_data = []
        for node in self.nodes:
            requests.pakages.urllib3.disable_warnings()
            self.session.headers.update(token)
            url = f'https://{self.switch["ip"]}/api/node/mo/topology/pod-1/node-{node}/sys/ch/supslot-1/sup.json'
            response = self.session.get(url)
            if response.status_code == 200:
                general = response.json()['imdata'][0]['eqptSupC']['attributes']
                print(f"{node} get General : ok")
            else:
                print(f"{node} get General : Failed")
                exit()
            url2 = f'https://{self.switch["ip"]}/api/{node}/class/firmwareRunning.json'
            response2 = self.session.get(url2)
            if response.status_code == 200:
                general = response.json()['imdata'][0]['firmwareRunning']['attributes']
                print(f"{node} get Version : ok")
            else:
                print(f"{node} get Version : Failed")
                exit()
            sum_data = general | version
            general_data.append(sum_data)
        return general_data
    
    def citrix(self, token):
        general_data = []
        sum_data = []
        uri_info = ['nsversion', 'nshardware', 'nsconfig', 'nshostname']
        requests.pakages.urllib3.disable_warnings()
        self.session.headers.update(token)
        for uri in uri_info:
            url = f'https://{self.switch["ip"]}/nitro/v1/config/{uri}'
            response = self.session.get(url)
            if response.status_code == 200:
                data = response.json()[f'{uri}']
                general_data.append(data)
                print(f"{self.switch['name']} Get {uri} : ok")
                return cpu_data
            else:
                print(f"{self.switch['name']} Get General : Failed")
                return None
        return general_data
    
    def cisco(self, ssh_client):
        commands = ["show version | begin Base"]
        if ssh_client:
            for command in commands:
                stdin, stdout, stderr = ssh_client.exec_command(command)
                time.sleep(1)
                general_data = stdout.read().decode('utf-8')
                print(f"{self.switch['name']} Get General : ok")
                ssh_client.close()
                return general_data
        else:
            print(f"{self.switch['name']} Get General : Failed")
            return None