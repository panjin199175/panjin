#-*- coding: utf-8 -*-

def custClick(self):
        #点击客户
    self.a.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul[1]/li[2]/a").click()

def custAdd(self):
    self.a.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div/a").click()#新建客户

def inputCustName(self,custName):
    self.a.find_element_by_xpath("//*[@id='name']").send_keys(custName)#客户名

def inputTel(self,Tel):
        #手机号
    self.a.find_element_by_xpath("//*[@id='form1']/table/tbody/tr[10]/td[4]/input").send_keys(Tel)

def custSubmit(self):
    #点击保存
    self.a.find_element_by_xpath("//*[@id='form1']/table/tfoot/tr/td/input[1]").click()

def windowsClick(self):
    #点击提示框
    self.a.switch_to_alert().dismiss()

def ownerShip(self):
    #点击公司性质
    self.a.find_element_by_xpath("//*[@id='ownership']").click()