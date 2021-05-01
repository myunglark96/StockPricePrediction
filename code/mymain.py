import win32com.client
import pythoncom

class XASessionEventHandler:
    login_state = 0

    def OnLogin(self, code, msg):
        if code == "0000":
            print("로그인 성공")
            XASessionEventHandler.login_state = 1
        else:
            print("로그인 실패")

class XAQueryEventHandler:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandler.query_state = 1

# ===================================================================================================================
instXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEventHandler)

with open('account.txt') as f:
    id, passwd, cert_passwd = f.read().split()

instXASession.ConnectServer("hts.ebestsec.co.kr", 20001)
instXASession.Login(id, passwd, cert_passwd, 0, 0)

while XASessionEventHandler.login_state == 0:
   pythoncom.PumpWaitingMessages()


