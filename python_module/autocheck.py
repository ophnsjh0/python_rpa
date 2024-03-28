from python_module.session.session_manager import SessionManager
from python_module.login import Login
from python_module.logout import Logout
from python_module.getdata.get_interface import GetInterface
from python_module.getdata.get_cpu import GetCpu
from python_module.getdata.get_mem import GetMem
from python_module.getdata.get_log import GetLog
from python_module.getdata.get_general import GetGeneral
from python_module.getdata.get_fan import GetFan


db = []

if __name__ == "__main__":
    ## 장비 정보 받아오기 ## 
    for switch in db:
        session_manager = SessionManager()
        session = session_manager.get_session()
        login = Login(switch, session)
        logout = Logout(switch, session)
        interface = GetInterface(switch, session)
        cpu = GetCpu(switch, session)
        mem = GetMem(switch, session)
        log = GetLog(switch, session)
        general = GetGeneral(switch, session)
        fan = GetFan(switch,session)
        
        ## 장비 종류별 점검 ## 
        if switch['model'] == "aci":
            token = login.aci()
            interface_data = interface.aci(token)
            cpu_data = cpu.aci(token)
            mem_data = mem.aci(token)
            log_data = log.aci(token)
            general_data = general.aci(token)
            fan_data = fan.aci(token)
            logout.aci
        elif switch['model'] == "citrix":
            login.citrix()
            interface_data = interface.citrix(token)
            cpu_data = cpu.citrix(token)
            mem_data = mem.citrix(token)
            log_data = log.citrix(token)
            general_data = general.citrix(token)
            logout.citrix()
        elif switch['model'] == "cisco":
            ssh_client = login.cisco()
            interface_data = interface.cisco(ssh_client)
            ssh_client = login.cisco()
            cpu_data = cpu.cisco(ssh_client)
            ssh_client = login.cisco()
            mem_data = mem.cisco(ssh_client)
            ssh_client = login.cisco()
            log_data = log.cisco(ssh_client)
            ssh_client = login.cisco()
            general_data = general.cisco(ssh_client)