#!/usr/bin/env python
# -*- coding: utf-8 -*-

num = input("Please enter numbers: ")
num_time = input("Please enter numbers: ")


def is_num(n):        # 定义函数  判断是不是数字
    if isinstance(n, (int, float)):
        return True
    else:
        for i in n:
            if i not in "-0123456789.":
                return False
        return True

count = 0

if is_num(num) and is_num(num_time):
    for i in range(1, int(num_time)+1):
        # print(i)
        print(str(num)*i)
        count += int(str(num)*i)
    print(count)
else:
    print("Please enter numbers!")
