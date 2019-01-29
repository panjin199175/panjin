#-*- coding: utf-8 -*-

def custRight(self):
        b=self.a.find_element_by_xpath("/html/body/div[5]/div[2]").text
        if b ==u"""×
添加客户成功""":
            print u"正确客户名测试通过"
        else:
            print u"正确客户名测试失败"

def custError(self):
        c=self.a.find_element_by_xpath("//*[@id='nameTip']").text
        if c ==u"该客户名称不可用，请更换客户名称":
            print u"重复的客户名测试通过"
        else:
            print u"重复的客户名测试失败"