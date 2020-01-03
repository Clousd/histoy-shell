
#!/usr/bin/python
#  coding:utf-8
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
#from PIL import Image
#from PIL import ImageGrab
import sys
import os
#设置默认字符集为UTF8 不然有些时候转码会出问题
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
        reload(sys)
        sys.setdefaultencoding(default_encoding)
#def _format_addr(s):
#       name, addr = parseaddr(s)
#       return formataddr((Header(name, 'utf-8').encode(), addr))
#发送邮件的相关信息，根据你实际情况填写
smtpHost =      "smtp.sina.cn"
#smtpPort = 25
sslPort  = 465
fromMail = 'log_python@sina.cn'
toMail   = ['kate.an@aliyun.com']#,'hll@xaito.com']
username = 'log_python@sina.cn'
password = '295815d767b23f5f'



#邮件标题和内容

subject  = u'提醒邮件'+str(time.strftime("%Y-%m-%d", time.localtime()))
#for line in open("/usr/local/apache2/logs/access_log"):
#       if u'28/Jul/2019:11' in line:
#               body = body+line

body = "代办事项"
#初始化邮件
encoding = 'utf-8'
mail = MIMEMultipart()
#mail = MIMEText(body.encode(encoding),'plain',encoding)
mail.attach(MIMEText(body.encode(encoding),'plain',encoding))
mail['Subject'] = Header(subject,encoding)
mail['From'] = fromMail
mail['To'] =  ','.join(toMail)
#im = ImageGrab.grab()

#im.save(addr,'test.jpeg')
#att1 = MIMEText(open('mail', 'r').read(), 'base64', 'utf-8')
#att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
#att1["Content-Disposition"] = 'attachment; filename="test.jpeg"'
#mail.attach(att1)
#mail['Date'] = formatdate()

try:
    #连接smtp服务器，明文/SSL/TLS三种方式，根据你使用的SMTP支持情况选择一种
    #普通方式，通信过程不加密
#       smtp = smtplib.SMTP(smtpHost,smtpPort)
#       smtp.ehlo()
#       smtp.login(username,password)

    #tls加密方式，通信过程加密，邮件数据安全，使用正常的smtp端口
    #smtp = smtplib.SMTP(smtpHost,smtpPort)
    #smtp.set_debuglevel(True)
    #smtp.ehlo()
    #smtp.starttls()
    #smtp.ehlo()
    #smtp.login(username,password)

    #纯粹的ssl加密方式，通信过程加密，邮件数据安全
        smtp = smtplib.SMTP_SSL(smtpHost,sslPort)
        smtp.ehlo()
        smtp.login(username,password)

    #发送邮件
        smtp.sendmail(fromMail,mail['To'].split(','),mail.as_string())
        smtp.close()
        print('OK')
except Exception as e:
        print (e)
