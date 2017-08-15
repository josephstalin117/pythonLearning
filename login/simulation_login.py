# coding: utf-8
import requests

if __name__ == '__main__':
    data = {
        'email': 'x@yunshan.net.cn',
        'password': 'admin'
    }
    s = requests.session()
    header_info = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Host': '10.25.0.10',
        'Connection': 'keep-alive',
        'Referer': 'https://10.25.0.10/',
        'appkey': '5ee218a0-25ec-463a-81f5-6c5364707cda'
    }

    content = s.post('https://10.25.0.10/api/login', data, verify=False)
    r = s.get('https://10.25.0.10/#/wanAnalysis/realtime', headers=header_info)
    print r

    import json

    body = {"url": "1/user-ip-resources", "objtype": "epc", "apitype": "app", "method": "get", "userid": 1}
    echo = s.get('https://10.25.0.10/appserver', params=json.dumps(body), headers=header_info)
    print echo, echo.text
