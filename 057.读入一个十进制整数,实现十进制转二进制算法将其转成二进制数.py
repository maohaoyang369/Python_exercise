#!/usr/bin/env python
# -*- coding: utf-8 -*-

num_decimal = int(input("Please enter numbers: "))


def dinary(num_decimal):
    num_list = []
    if num_decimal < 0:
        return '-' + dinary(abs(num_decimal))       # abs() 绝对值
    elif num_decimal >= 0:
        while True:
            temp = num_decimal % 2
            num_decimal = num_decimal // 2      # 取整
            num_list.append(str(temp))
            if num_decimal == 0:
                break
        return "".join(num_list[::-1])

print(dinary(num_decimal))

