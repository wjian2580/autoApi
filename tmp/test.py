import requests
r = requests.request('post','http://localhost:5001/login',data={'username':'admin','password':'123456'})
print(r.text)
print(str(r.elapsed.microseconds // 1000) + 'ms')