#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 检测用户是否输入了一个非整数的字（try except）

number = input("请输入一个整数: ")

def collatz(number):
    try:
        if int(number) % 2 == 0:
            return int(number)//2
        elif int(number) % 2 == 1:
            return 3 * int(number) + 1
    except:
        return("请输入整数！")        # 当为print("请输入整数！") 时，结果会输出None

print(collatz(number))