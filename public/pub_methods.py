from .config import base_url
class ApiInvoke(object):
	
	def get(self,url,params,headers,timeout):
		response = requests.get(url=url,params=params,headers=headers,timeout=timeout)
		return response
	
	def post(self,username,password):
		response = requests.get(url=url,params=params,headers=headers,timeout=timeout)	
		return requests.post(url,data=data).cookies.get('session')
