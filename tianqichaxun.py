# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:42:20 2018

@author: lenovo
"""

import urllib.request as r
import json
city_pinyin = input("请输入城市拼音:")
print(city_pinyin)
address = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
print(address.format(city_pinyin))
#1、查看当前城市天气2、查看其他城市天气3、保存当前城市天气

print("欢迎使用")
print("1、查看当前城市天气2、查看其他城市天气3、保存当前城市天气")
menno = input("请输入菜单")
if menno=='1':
    print("1、查看当前城市天气");
    info = r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
    data = json.loads(info)
    temp = data["main"]["temp"]
    pressure = data["main"]["pressure"]
    weather = data["weather"]
    des = weather[0]
    description = des["description"]
    print(city_pinyin+"天气情况如下")
    print("温度:"+str(temp))
    print("气压:"+str(pressure))
    print("状况:"+str(description))
    

if menno=='2':
    print("2、查看其他城市天气");
if menno=='3':
    print("3、保存当前城市天气");