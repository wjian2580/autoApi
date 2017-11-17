#!/usr/bin/python
# coding=utf-8

import unittest,os,time
from HTMLTestRunner import HTMLTestRunner
from public import send_mail

day = time.strftime("%Y-%m-%d")
time = time.strftime("%H_%M_%S")

root = os.path.split(os.path.realpath(__file__))[0]+os.sep
case_dir = os.path.join(root,'test_case')
result_dir = os.path.join(root,'test_result')
report_dir = os.path.join(result_dir,day)
file_name = time + '-result.html'
report = os.path.join(report_dir,file_name)

if not os.path.exists(report_dir):
	os.mkdir(report_dir)

fp = open(report,'wb')
cover = unittest.defaultTestLoader.discover(case_dir,pattern='test*.py')
runner = HTMLTestRunner(stream=fp,title='System-Service接口自动化测试报告',description='测试结果：')

if __name__ == '__main__':
	runner.run(cover)
	fp.close()
	# with open(report,'rb') as f:
	# 	html = f.read()
	# if html:
	# 	send_mail.send(html)


