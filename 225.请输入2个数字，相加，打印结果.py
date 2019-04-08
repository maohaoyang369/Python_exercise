# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 请输入2个数字，相加，打印结果
# （不管用户输入什么，程序不能崩溃）输入输入的不是数字，那么让用户在重新输入。
# 提示用while死循环。

result = ""


while 1:
    try:
        a = float(input("请输入数据a:"))
        break
    except:
        print("输入的数据不是数字类型，请重新输入。")

while 1:
    try:
        b = float(input("请输入数据b:"))
        break
    except:
        print("输入的数据不是数字类型，请重新输入。")

result = a+b

print(result)
