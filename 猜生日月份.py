#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 猜生日月份

birth_month = input("请输入你的生日月:")
if int(birth_month) == 7:
    print ("当月是你的生日月")
elif  7 < int(birth_month) <= 12 or 1 <= int(birth_month) < 7:
    print("当月不是你的生日月")
else:
    print("非法字符")