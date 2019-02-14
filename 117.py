# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 用户输入不同的数据，当输入的数据达到3个数字的时候，求和结束程序。（数字可以是整数）

# 提示：判断是否整数的方法，isdigit()
# 遍历所有的输入数据，判断是否在0-9的字符串范围内


def num_int(num):        # 判断输入的数据是否是整数的方法
    for i in num:
        if i not in "0123456789":
            return False
    return True


total = 0
count = 0
while True:
    sentence = input("请输入数据：")
    if num_int(sentence):
        total += int(sentence)
        count += 1
        if count == 3:
            break
    else:
        print("False")
print(total)
