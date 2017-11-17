#!/usr/bin/python
# coding=utf-8
import sys
sys.path.append('C:\\Users\\wang\\Desktop\\autoapi')
import requests,unittest
from apiss.api import ApiInvoke

class TestApi(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.username = 'admin'
		cls.password = '123456'
		cls.api = ApiInvoke()
	def test_login(self):
		res = self.api.login(self.username,self.password)
		assert res['code'] == '200'
		assert res['msg'] == 'success'
	def test_info(self):
		cookie = self.api.get_cookies(self.username, self.password)
		cookies = {
			'session': cookie
		}
		print (cookies)
		res = self.api.info(cookies=cookies)
		assert res['code'] == '200'
		assert res['msg'] == 'success'
		assert res['data'] == 'info'

if __name__ == '__main__':
	unittest.main()