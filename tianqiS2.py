# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:35:34 2018

@author: lenovo
"""
#{}代表占位符
import urllib.request as r
import json
print("欢迎使用_查看当前城市天气")
city_pinyin = input("请输入城市拼音:")
print(city_pinyin)
address = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
print(address.format(city_pinyin))
info = r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
data = json.loads(info)
temp = data["main"]["temp"]
pressure = data["main"]["pressure"]
weather = data["weather"]
des = weather[0]
description = des["description"]
print(city_pinyin+"天气情况如下")
print("温度:"+str(temp)+"华氏摄氏度")
print("气压:"+str(pressure)+"帕")
print("状况:"+str(description))
input("输入任意退出·........")

  

     
    

