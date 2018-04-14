#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-14 18:37:55
# @copyright by hoojo@2018
# @changelog Added python3 `email -> send mail image` example


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

host = "smtp.qq.com"
user = 'hoojo@qq.com'
passwd = 'xxx'  # 发件人邮箱密码(当时申请smtp给的口令)

sender = user  # 发件人邮箱账号
recv = 'hoojo@qq.com'  # 收件人邮箱账号，我这边发送给自己

content = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.hoojo.cn">这是一个链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""

def mail():
    ret = True
    
    try:
        #创建一个带附件的实例
        message = MIMEMultipart('related')
        message['From'] = formataddr(["发件人昵称", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        message['To'] = formataddr(["收件人昵称", recv])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        message['Subject'] = Header("邮件主题-测试", 'utf-8')  # 邮件的主题，也可以说是标题
        
        text = MIMEMultipart('alternative')
        # 邮件正文内容
        text.attach(MIMEText(content, 'html', 'utf-8'))
        # 添加正文
        message.attach(text)
        
        # 指定图片为当前目录
        fp = open('test.png', 'rb')
        image = MIMEImage(fp.read())
        fp.close()
        
        # 定义图片 ID，在 HTML 文本中引用
        image.add_header('Content-ID', '<image1>')
        # 邮件图片附件
        message.attach(image)
        
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
