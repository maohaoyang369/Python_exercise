#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Collatz 序列（让用户输入一个整数，并不断对这个数调用 collatz()，直到函数返回值1）

number_in = input("请输入一个整数: ")
number = int(number_in)

def collatz(number):        # 定义一个函数 参数为number
    if number % 2 == 0:        # 如果输入的整数为偶数，取整
        return number//2
    elif number % 2 == 1:        # 如果输入的整数为奇数，求3 * number + 1值
        return 3 * number + 1

print(collatz(number))