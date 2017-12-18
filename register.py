#coding=utf-8
import requests
import pdb
requests.packages.urllib3.disable_warnings()
url = 'https://111.13.63.1:9801/api/auth/regist/100000/'
data = {
    "cpid" : "600213",
    "device_id" : "DE468F7C-EEED-4A9D-B29B-DFD54ADF55FC",
    "cmdVersion" : "1",
    "phone_num" : "EEiBsCoNjNp5FW3KfOOGsw%3D%3D"
}
r = requests.post(url,json=data,verify=False)
pdb.set_trace()
res = r.json()
code = res['sec_code']
print(code)

loginData = {
    "sec_code" : code,
    "device_id" : "DE468F7C-EEED-4A9D-B29B-DFD54ADF55FC",
    "invitation_code" : "",
    "phone_num" : "18310602997"
}
loginUrl = 'https://111.13.63.1:9801/api/auth/login/100000/'
loginHeaders = {
	"User-Agent": "ZhongXinJianTou_Phone/2.6.0 (iPhone; iOS 11.1.2; Scale/3.00)",
	"X-Tingyun-Id": "p35OnrDoP8k;c=2;r=1436197548"
}
s = requests.session()
login = s.post(loginUrl,json=loginData,headers=loginHeaders,verify=False)
print(login.text)
#print(login.raw)

userinfoUrl = 'http://111.13.63.1:9800/api/system/user/info/select'
payload = {
	"userId":101302
}
info = s.post(userinfoUrl,json=payload).json()
print(info)


