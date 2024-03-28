import paramiko
import requests
import json
import time
from json.decoder import JSONDecoder
from datetime import datetime

class GetLog:
    def __init__(self, switch, session):
        self.switch = switch
        self.session = session
        self.session.verify = False
        self.nodes = ["1101", "1102", "1201"]
         
    def aci(self, token):
        for node in self.nodes:
            requests.pakages.urllib3.disable_warnings()
            self.session.headers.update(token)
            url = f'https://{self.switch["ip"]}/api/node/class/faultSummary.json'
            response = self.session.get(url)
            if response.status_code == 200:
                log_data = response.json()['imdata']
                print(f"{node} get Log : ok")
                return log_data
            else:
                print(f"{node} get Log : Failed")
                exit()
        return interfaces_data
    
    def citrix(self, token):
        log_data = []
        requests.pakages.urllib3.disable_warnings()
        self.session.headers.update(token)
        url = f'https://{self.switch["ip"]}/nitro/v1/config/nsevents'
        response = self.session.get(url)
        if response.status_code == 200:
            event = response.json()
            for event in events['nsevents']:
                timestamp = event['time']
                now = datetime.now()
                now_date = now.strftime("%Y-%m-%d")
                event_date_str = datetime.utcfromtimestamp(int(timestamp))
                event_date = event_date_str.strftime("%Y-%m-%d")
                if event_date == now_date:
                    log_data.append(event)
            print(f"{self.switch['name']} Get Log : ok")
            return log_data
        else:
            print(f"{self.switch['name']} Get Log : Failed")
            return None
    
    def cisco(self, ssh_client):
        now = datetime.now()
        formatted_date = now.strftime("%b %d")
        commands = [f"show logging | inc {formatted_date}"]
        if ssh_client:
            for command in commands:
                stdin, stdout, stderr = ssh_client.exec_command(command)
                time.sleep(1)
                log_data = stdout.read().decode('utf-8')
                print(f"{self.switch['name']} Get Log : ok")
                ssh_client.close()
                return log_data
        else:
            print(f"{self.switch['name']} Get Log : Failed")
            return None