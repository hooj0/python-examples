#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-14 17:01:36
# @copyright by hoojo@2018
# @changelog Added python3 `email -> send mail2` example


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

host = "smtp.qq.com"
user = 'hoojo@qq.com'
passwd = 'xxx'  # 发件人邮箱密码(当时申请smtp给的口令)

sender = user  # 发件人邮箱账号
recv = 'hoojo@qq.com'  # 收件人邮箱账号，我这边发送给自己

def mail():
    ret = True
    
    try:
        message = MIMEText('填写邮件内容', 'plain', 'utf-8')
        message['From'] = formataddr(["发件人昵称", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        message['To'] = formataddr(["收件人昵称", recv])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        message['Subject'] = Header("邮件主题-测试", 'utf-8')  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP(host, 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.set_debuglevel(1)
        server.login(user, passwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, [recv, ], message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print('Error: %s' % e)
        ret = False
    return ret

ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
