#!/usr/bin/python
# coding=utf-8

import unittest
import os,time
from HTMLTestRunner import HTMLTestRunner


case_dir = os.path.join(os.getcwd(),'test_case')
now_time = time.strftime("%Y-%m-%d")
os.mkdir('./test_result/'+now_time)
report = './test_result/' + now_time + '/result.html'
fp = open(report,'wb')
cover = unittest.defaultTestLoader.discover(case_dir,pattern='test*.py')
runner = HTMLTestRunner(stream=fp,title='Test Result',description='Test Case Executive Condition:')

if __name__ == '__main__':
	runner.run(cover)
	fp.close()
