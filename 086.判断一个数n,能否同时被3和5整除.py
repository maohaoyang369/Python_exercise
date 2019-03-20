#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 判断一个数n，能否同时被3和5整除

n = input("please input number：")
if float(n) % 3 == 0 and float(n) % 5 == 0:
    print("This is the right number")
else:
    print("This is the worng number") 