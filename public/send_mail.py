from email.mime.text import MIMEText
from email.header import Header
import time
import smtpli

from_addr = 'wjian2580@163.com'
password = 'Wjian2580'
to_addr = ['501260495@qq.com','wangjian0414@rayootech.com']
smtp_server = 'smtp.163.com'
now_time = time.strftime("%Y-%m-%d %H-%M-%S")
msg = MIMEText(, 'plain', 'utf-8')
msg['Subject'] = Header(now_time+'接口测试报告', 'utf-8').encode()
msg['From'] = from_addr
for receiver in to_addr:
	msg['To'] = receiver
server = smtplib.SMTP(smtp_server, 25) 
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
print('发送成功')