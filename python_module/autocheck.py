from python_module.session.session_manager import SessionManager
from python_module.login import Login
from python_module.logout import Logout
from python_module.getdata.get_interface import GetInterface

db = []

if __name__ == "__main__":
    ## 장비 정보 받아오기 ## 
    for switch in db:
        session_manager = SessionManager()
        session = session_manager.get_session()
        login = Login(switch, session)
        logout = Logout(switch, session)
        interface = GetInterface(switch, session)
        
        ## 장비 종류별 점검 ## 
        if switch['model'] == "aci":
            token = login.aci()
            interface.aci(token)
            logout.aci
        elif switch['model'] == "citrix":
            login.citrix()
            logout.citrix()
        elif switch['model'] == "cisco":
            ssh_client = login.cisco()
            result = interface.cisco(ssh_client)
            logout.cisco(ssh_client)