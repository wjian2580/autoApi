#!/usr/bin/python
# coding=utf-8

import unittest
import requests
from public import cp_api,cpm
from public import log

class Request(object):
	def __init__(self,api_name):
		self.api_name = api_name
		self.url = cpm.get('env', 'host') + ':' + cpm.get('env', 'http_port') + cp_api.get(api_name,'api')
		self.method = cp_api.get(api_name, 'method')
		self.data = cp_api.get(api_name, 'data')
	
	def req(self):
		logs = log.Log()
		logs.info('------------'+ self.api_name + ' -Test-Start---------')
		api = {
			'url' : self.url,
			'method' : self.method,
			'data' : self.data
		}
		logs.info('api_info : %s' % api)
		r = requests.request(method=self.method,url=self.url,data=self.data)
		logs.info('code : %s' % r.status_code)
		logs.info('json : %s' % r.json())	
		return r
