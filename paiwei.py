# 2018年越秀区小学升初中电脑派位结果查询




# -*- coding:utf-8 -*-
import requests
import re
import time

url = 'http://121.8.163.26/Default.aspx'
numbers = []
for i in range(446001, 446132):
    numbers.append(i)
for i in range(448001, 448132):
    numbers.append(i)
params = {
    b"__VIEWSTATEGENERATOR": 'CA0B0334',
    b"__EVENTVALIDATION": '/wEWAwL0tK2ZBQLzmsb0DQKNmeLvDdtaFFgf8QjaW9+Q8be3Sxj+cS9Y',
    b"__VIEWSTATE": '/wEPDwULLTEwODI2ODM5NTEPZBYCAgEPZBYCAgMPDxYCHgdWaXNpYmxlaGRkZFU8PNcvtIBxGo8tKHpNYdZy0vDK',
    b"CXBtn": '查询录取结果',
}
for i in numbers:
    params[b"KHBox"] = i
    req = requests.post(url, data=params)
    res = re.search('<span id="KHLabel".*?>(.*?)</span>.*?<span id="NameLabel".*?>(.*?)</span>.*?<span id="SexLabel".*?>(.*?)</span>.*?<span id="ByLabel".*?>(.*?)</span>.*?<span id="SchoolLabel".*?>(.*?)</span>', req.text, re.S)
    try:
        print(res.group(1), res.group(2), res.group(3), res.group(4), res.group(5))
    except:
        print(i, "null", "null", "null", "null")
    time.sleep(2.5)















































