#-*- coding: utf-8 -*-
from selenium import webdriver

def openWeb(self):
    self.a=webdriver.Chrome()#打开浏览器

def inputUrl(self):
    self.a.get("http://120.76.119.135/wk")#输入url

def inputUserName(self,userName):
    self.a.find_element_by_name("name").send_keys(userName)#输入用户名

def inputPasswd(self,passWd):
    self.a.find_element_by_name("password").send_keys(passWd)#输入密码

def submit(self):
    self.a.find_element_by_name("submit").click()#点击登录

