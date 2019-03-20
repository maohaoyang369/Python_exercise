#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 假定你希望程序保存朋友生日的数据，就可以使用一个字典，用名字作为键，用生日作为值

birthdays = {'Alice': 'Apr 1','Bob': 'Dec 12','Carol': 'Mar 4'}        # 定义一个字典

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':        # 当输入的name为空时，跳出循环
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)        # 当输入的名字在字典中时，输出生日日期
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()   # 当输入的名字不在字典中时，将输入此人的生日，作为字典的键值，当再次输入该名字时，就可以知道这个朋友的生日了
        birthdays[name] = bday
        print('birthday database updated.')

