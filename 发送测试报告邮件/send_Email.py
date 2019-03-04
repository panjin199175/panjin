#!/usr/local/bin/python3
#coding:utf-8
# @Time    : 2019/3/4 14:20
# @Author  : Hollow
# @FileName: send_Email.py
# @Software: PyCharm

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#-----------1.跟发邮件相关的参数--------
smtpserver = "smtp.qq.com"   #发件服务器
port =465   #端口
sender = "392799576@qq.com"   #账号
psw = "udysiyygyslpbjcj"   #授权密码
#receiver = ['15820226692@163.com']   #单个接收人也可以是list
receiver = ["15820226692@163.com","392799576@qq.com"]   #多个收件人list对象


#-----------2.编辑邮件内容-------
#读文件
file_path = "pj.html"
with open(file_path,"rb") as fp:
    mail_body = fp.read()
msg = MIMEMultipart()
msg["from"] = sender              #发件人
msg["to"] = ";".join(receiver)    #多个收件人list转str
msg["subject"] = "这个是我的测试报告"    #主题
#正文
body = MIMEText(mail_body,"html","utf-8")
msg.attach(body)
#附件
att = MIMEText(mail_body,"base64","utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="test_report.html"'
msg.attach(att)


#-----------3.发送邮件------------
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)      #连接服务器
    smtp.login(sender,psw)
except:
    smtp = smtplib.SMTP_SSL(smtpserver,port)
    smtp.login(sender,psw)         #登录
smtp.sendmail(sender,receiver,msg.as_string())  #发送
smtp.quit()     #关闭

