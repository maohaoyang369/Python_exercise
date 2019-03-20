#!/usr/bin/env python
# # -*- coding: utf-8 -*-

# 检查ipV4的有效性，有效则返回True，否则返回False，（提示使用split函数进行分割）

ip_v = "10.60.192.168"

for i in ip_v:
    # print(i)
    if not isinstance(i, str):
        print(False)
    elif (ip_v).count('.') != 3:
        print(False)

ip_split = ip_v.split('.')

if ip_split[0] == "0":
    print(False)

for j in ip_split:
    # print(j)
    if int(j) >= 0 and int(j) <= 255:
        continue
    else:
        print(False)







