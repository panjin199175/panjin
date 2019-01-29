#-*- coding: utf-8 -*-

def loginRight(self):
        #登录成功后，获取提示信息的文本内容
        b=self.a.find_element_by_xpath("/html/body/div[5]/div[2]").text
        if b==u"""×
登录成功""":
                print u"登录测试成功"
        else:
                print u"登录测试失败"

def loginError(self):
        #登录失败后，获取提示信息的文本内容
        c=self.a.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/form/fieldset/div").text
        if c==u"""×
用户名或密码错误！""":
                    print u"登录测试成功"
        else:
                    print u"登录测试失败"

def loginNull(self):
        #空密码失败后，获取提示信息的文本内容
        c=self.a.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/form/fieldset/div").text
        if c==u"""×
请正确输入用户名和密码！""":
                    print u"登录测试成功"
        else:
                    print u"登录测试失败"
