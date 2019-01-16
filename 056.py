#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 让用户输入一个宠物名字，然后检查该名字是否在宠物列表中

pets = ['Hay', 'Bell', 'Cabage']
name = input("input pets name:")
if name in pets:
    print(name + ' is my pet.')
else:
    print(name + " is not my pet.")