#!/usr/bin/python
# coding=utf-8
import requests
from config import base_url

json = {"sessionid": "Z"}

params = {"req_funType":"L295","req_sinceId":"0","req_count":"1"}
r = requests.request('post','http://111.13.63.2:9800/api/trade/ptjy/ptyw/cxxtzt',json = json)
print(r.text)
print(str(r.elapsed.microseconds // 1000) + 'ms')
