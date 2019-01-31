#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入5个名字，排序后输出

names = []
for i in range(1,6):
    name = input("Enter a name: ")
    if name == '':
        break
    if name in names:
        print("Repeated names!")
    else:
        names = names + [name]
names.sort()        # 排序 按ASCII码
print(names)