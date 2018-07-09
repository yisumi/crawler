# -*- coding:utf-8 -*-
# author: yisumi
# create_time: 2018/7/9,11:47
# file_name: paiweichaxun.py
# ide_name: PyCharm Community Edition
# comments: 2018年越秀区小学升初中电脑派位结果查询:http://121.8.163.26/Default.aspx
# 通过输入电脑号查询出结果
# ------------------------------------------------------------------------------------------------------
import requests
import re
import time

url = 'http://121.8.163.26/Default.aspx'
numbers = []
for i in range(446001, 446132):
    numbers.append(i)
for i in range(448001, 448132):
    numbers.append(i)
# 请求所需参数，通过badboy工具获得
params = {
    b"__VIEWSTATEGENERATOR": 'CA0B0334',
    b"__EVENTVALIDATION": '/wEWAwL0tK2ZBQLzmsb0DQKNmeLvDdtaFFgf8QjaW9+Q8be3Sxj+cS9Y',
    b"__VIEWSTATE": '/wEPDwULLTEwODI2ODM5NTEPZBYCAgEPZBYCAgMPDxYCHgdWaXNpYmxlaGRkZFU8PNcvtIBxGo8tKHpNYdZy0vDK',
    b"CXBtn": '查询录取结果',
    # 关键参数：电脑号
    b"KHBox": ''
}
for i in numbers:
    params[b"KHBox"] = i
    # 通过http的post方法获取查询结果。
    req = requests.post(url, data=params)
    # 使用正则表达式提取结果中的电脑号、姓名、性别、毕业学校、录取去向。
    res = re.search('<span id="KHLabel".*?>(.*?)</span>.*?<span id="NameLabel".*?>(.*?)</span>.*?<span id="SexLabel".*?>(.*?)</span>.*?<span id="ByLabel".*?>(.*?)</span>.*?<span id="SchoolLabel".*?>(.*?)</span>', req.text, re.S)
    try:
        print(res.group(1), res.group(2), res.group(3), res.group(4), res.group(5))
    except:
        print(i, "null", "null", "null", "null")
    # 每隔2.5秒查询一次。因为网站限制高频查询，经测试，2.5秒时间间隔可以避开限制。
    time.sleep(2.5)


