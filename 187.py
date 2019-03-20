# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入一个正整数，输出该正整数的阶乘的值

num_input = input("Please enter the number：")


def is_num(n):        # 定义函数  判断是不是数字
    if isinstance(n, (int, float)):
        return True
    else:
        for i in n:
            if i not in "0123456789":
                return False
        return True


def factorial(num):
    if not is_num(num):
        return False
    elif is_num(num):
        num = int(num)
        if num > 0:
            return num * factorial(num-1)
        else:
            return 1


print(str(num_input) + " 的阶乘是：" + str(factorial(num_input)))
