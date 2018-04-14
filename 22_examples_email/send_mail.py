#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-14 14:55:33
# @copyright by hoojo@2018
# @changelog Added python3 `email -> send mail` example


from email.mime.text import MIMEText
from email.header import Header
import smtplib
from email.utils import parseaddr, formataddr

'''
使用第三方服务器发送邮件
'''

# 第三方SMTP服务
host = 'stmp@126.com'
user = 'hoojo_@126.com'
passwd = 'xxx'

# 发送人
sender = 'from@qq.com'
# 接收人
recveres = [ 'hoojo@qq.com' ]

charset = 'utf-8'

message = MIMEText('python 发送邮件测试', 'plain', charset)
message['From'] = formataddr(['Python From', 'aaa'])
message['To'] = formataddr(['Python To', 'bbb'])
#message['From'] = Header('Python send', charset)
#message['To'] = Header('revc python', charset)
message['Subject'] = Header('这是一份测试邮件', charset)

try:
    server = smtplib.SMTP_SSL()
    server.set_debuglevel(1)
    
    # 连接到stmp服务器
    server.connect(host, 25) # 25 为stmp 端口号
    # 登录到smtp服务器
    server.login(user, passwd)
    
    # 发送邮件
    server.sendmail(user, recveres, message.as_string())
    
    # 退出
    server.quit()
except smtplib.SMTPException as e:
    print('发送邮件错误：%s', e)    
