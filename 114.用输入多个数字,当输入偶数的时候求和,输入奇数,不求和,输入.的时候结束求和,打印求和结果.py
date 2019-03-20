# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 用输入多个数字，当输入偶数的时候求和，输入奇数，不求和，输入.的时候结束求和，打印求和结果

count_even = 0
while True:
    num = input("Please enter num：")
    if num == ".":
        break
    else:
        if int(num) % 2 == 0:
            count_even += int(num)
print(count_even)
