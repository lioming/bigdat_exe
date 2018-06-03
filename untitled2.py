# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:58:36 2018

@author: lenovo
"""
import urllib.request as m
print("请输入城市")
city = input("城市拼音：")
address = "http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996"
information = m.urlopen(address.format(city)).read().decode("utf-8","ignore")

