
from control_login import openWeb,inputUrl,inputUserName,inputPasswd,submit
from business_login import  loginRight,loginError,loginNull
from data import ReadExcel

class loginTestcase():
    def __init__(self):
        openWeb(self)
        inputUrl(self)

    def testcase1(self):
        u=ReadExcel(0,1,2)
        inputUserName(self,u)
        p=ReadExcel(0,1,3)
        p_new=int(p)
        inputPasswd(self,p_new)
        submit(self)
        loginRight(self)

    def testcase2(self):
        u=ReadExcel(0,2,2)
        inputUserName(self,u)
        p=ReadExcel(0,2,3)
        p_new=int(p)
        inputPasswd(self,p_new)
        submit(self)
        loginRight(self)

    def testcase3(self):
        u=ReadExcel(0,3,2)
        inputUserName(self,u)
        p=ReadExcel(0,3,3)
        p_new=int(p)
        inputPasswd(self,p_new)
        submit(self)
        loginError(self)

    def tesecase4(self):
        u=ReadExcel(0,4,2)
        inputUserName(self,u)
        p=ReadExcel(0,4,3)
        inputPasswd(self,p)
        submit(self)
        loginNull(self)


loginTestcase().testcase1()
loginTestcase().testcase2()
loginTestcase().testcase3()
loginTestcase().tesecase4()
