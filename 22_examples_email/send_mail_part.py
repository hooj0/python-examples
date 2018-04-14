#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-14 18:23:50
# @copyright by hoojo@2018
# @changelog Added python3 `email -> send mail part` example


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email.mime.multipart import MIMEMultipart

host = "smtp.qq.com"
user = 'hoojo@qq.com'
passwd = 'xxx'  # 发件人邮箱密码(当时申请smtp给的口令)

sender = user  # 发件人邮箱账号
recv = 'hoojo@qq.com'  # 收件人邮箱账号，我这边发送给自己

content = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.hoojo.cn">这是一个链接</a></p>
"""

def mail():
    ret = True
    
    try:
        #创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = formataddr(["发件人昵称", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        message['To'] = formataddr(["收件人昵称", recv])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        message['Subject'] = Header("邮件主题-测试", 'utf-8')  # 邮件的主题，也可以说是标题
        
        # 邮件正文内容
        message.attach(MIMEText(content, 'html', 'utf-8'))
        
        # 构造附件1，传送当前目录下的 mail_stmp.py 文件
        att1 = MIMEText(open('mail_stmp.py', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="test.txt"'
        # 添加附件
        message.attach(att1)
        
        # 构造附件2，传送当前目录下的mail_stmp.py 文件
        att2 = MIMEText(open('mail_stmp.py', 'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename="test2.txt"'
        # 添加附件
        message.attach(att2)

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
