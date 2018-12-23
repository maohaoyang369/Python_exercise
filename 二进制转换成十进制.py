#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 二进制转换成十进制

bianary_number = input("请输入二进制数:")
length = len(bianary_number)
print(length)
result = 0
for i in range(length):
    result += int(bianary_number[i]) * pow(2, length-1-i)
    print(i)
    print(pow(2, length-1-i))
print(result)

