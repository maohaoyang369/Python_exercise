# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 记账程序，每天收入多少，支出多少，总额剩多少，使用序列化方式保存信息
# 写个记账程序，每天收入多少，支出多少，
# 总额剩多少，使用序列化方式保存信息

import pickle

fp = open("d:\\python\\a.txt", "rb")
try:
    income = pickle.load(fp)
    spend = pickle.load(fp)
    deposit = pickle.load(fp)
except:
    income = []
    spend = []
    deposit = 0
fp.close()

# value|specification
while 1:
    content = input("请输入指令：")
    if content.find("exit") != -1:
        break

    if content.find("|") == -1:
        print("data format is value|specification")
        print("please input again!")
        continue

    value = content.split("|")[0]
    try:
        value = float(value)
    except:
        print("data format is value|specification")
        print("data format is value must be a number")

    if value > 0:
        income.append(content)
        deposit += value
    elif value == 0:
        print("空间有限，不存0")
    else:
        spend.append(content[1:])
        deposit += value

print(income)
print(spend)
print(deposit)

fp = open("d:\\python\\a.txt", "wb")
pickle.dump(income, fp)
pickle.dump(spend, fp)
pickle.dump(deposit, fp)

fp.close()
