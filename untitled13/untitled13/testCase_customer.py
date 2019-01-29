from  control_login import openWeb,inputUrl,inputUserName,inputPasswd,submit
from control_customer import custClick,custAdd,inputCustName,inputTel,custSubmit,ownerShip,windowsClick
from data import ReadExcel
from business_customer import custRight,custError

class custTestCase():
    def __init__(self):
        openWeb(self)
        inputUrl(self)
        u=ReadExcel(0,1,2)
        inputUserName(self,u)
        p=ReadExcel(0,1,3)
        p_new=int(p)
        inputPasswd(self,p_new)
        submit(self)
        custClick(self)
        custAdd(self)
        custName=ReadExcel(1,1,2)
        inputCustName(self,custName)
        Tel=ReadExcel(1,1,3)
        inputTel(self,Tel)
        custSubmit(self)

    def testcase1(self):
        custRight(self)

    def testcase2(self):
        windowsClick(self)
        ownerShip(self)
        custError(self)

custTestCase().testcase1()
custTestCase().testcase2()