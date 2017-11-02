import unittest
import requests
from public import cp
from config import base_url
class MyRequest(object):

	def req(self,api_name):
		url = base_url + cp.get(api_name,'api')
		method = cp.get(api_name, 'method')
		data = cp.get(api_name, 'data')
		return requests.request(method=method,url=url,data=data)
