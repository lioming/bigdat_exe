# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:54:35 2018

@author: lenovo
"""

import urllib.request as r
import json
cityname = input("请输入需要查询天气的城市")
address1 = 'http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'
info1 = r.urlopen(address1.format(cityname)).read().decode("utf-8","ignore")
Tians = json.loads(info1)
days = Tians["list"]
day6 = days[0]
day5 = days[8]
day4 = days[16]
day3 = days[24]
day2 = days[30]
dayinfo = [day6,day5,day4,day3,day2]
for i in range(5):
     temp = dayinfo[i]["main"]["temp"]
     pressure = dayinfo[i]["main"]["pressure"]
     descrption = dayinfo[i]["weather"][0]["description"]
     print("今天是：星期"+str((i+6)%7))
     print("温度是："+str(temp))
     print("气压是："+str(pressure))
     print("天气情况是："+str(descrption))
     print("------------")
     
   
    
    






