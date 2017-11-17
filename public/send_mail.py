from email.mime.text import MIMEText
from email.header import Header
import time,smtplib
from public import cpm
from public import log

logger = log.Log()


def send(html):
	from_addr = cpm.get('mail', 'from_addr')
	to_addr = cpm.get('mail', 'to_addr').split(',')
	smtp_server = cpm.get('mail', 'smtp_server')
	password = cpm.get('mail', 'password')
	port = cpm.get('mail', 'port')
	now_time = time.strftime("%Y-%m-%d")
	msg = MIMEText(html, 'html', 'utf-8')
	msg['Subject'] = Header(now_time+'-接口测试报告', 'utf-8').encode()
	msg['From'] = from_addr
	for receiver in to_addr:
		msg['To'] = receiver
	server = smtplib.SMTP(smtp_server, port) 
	try:
		server.login(from_addr, password)
		returns = server.sendmail(from_addr, to_addr, msg.as_string())
		logger.info(returns)
	except Exception as e:
		logger.error(e)
		logger.info('邮件发送失败')
	server.quit()