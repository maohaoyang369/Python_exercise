# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 将字符串："k:1|k1:2|k2:3|k3:4"，处理成 python 字典：{'k':'1', 'k1':'2', 'k2':'3','k3':'4' }

sentance = "k:1|k1:2|k2:3|k3:4"

result = {}

a = sentance.split("|")        # 将字符串用“|”分隔开 生成列表

print(a)        # ['k:1', 'k1:2', 'k2:3', 'k3:4']

for i in a:
    key, value = i.split(":")
    result[key] = value

print(result)

# 字典：{'k': '1', 'k1': '2', 'k2': '3', 'k3': '4'}  拼回："k:1|k1:2|k2:3|k3:4"

sentance = {'k': '1', 'k1': '2', 'k2': '3', 'k3': '4'}

result = []

for m, n in sentance.items():
    result.append(m+":"+n)

print("|".join(result))

# 算法：
# 1 先把字典的key排序
# 2 然后按照排序后的key，依次取value，然后使用: 把key和value做拼接，然后把拼接后的结果存到一个列表里面
# 3 使用join，使用|将列表的所有元素做拼接

d = {'k': '1', 'k1': '2', 'k2': '3', 'k3': '4'}
result = []

for key in sorted(d.keys()):
    s = key+":"+d[key]
    result.append(s)

print(result)
print("|".join(result))
