#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入一个整数，输出其阶乘结果

num = int(input("Enter a number："))
factorial = 1

if num < 0 :
    print("抱歉，负数没有阶乘")
elif num == 0:
    print("0 的阶乘为 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("%d 的阶乘为 %d" %(num,factorial))