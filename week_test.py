# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:41:50 2018

@author: lenovo
"""

week = ["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]
print(week[5])
a = "星期六"
b = week[5]
#print('今天是{}')
for i in range(7):
  if week[i]=='星期六':
    print("今天是"+week[i])
  else:
      print(week[i])