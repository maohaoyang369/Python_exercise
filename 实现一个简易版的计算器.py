#/usr/bin/env python
# -*- coding: utf-8 -*-!

# 实现一个简易版的计算器，功能要求：加、减、乘、除，支持多数同时进行计算

# 第一种方法


def calculator(*args):
    help_infomation = \
    """
    1.加法
    2.减法
    3.乘法
    4.除法
    """
    print(help_infomation)
    result = 0
    command = input("Please enter: ")
    if command == "1":
        for i in args:
            result += i
    elif command == "2":
        for m in args:
            result -= m
    elif command == "3":
        result = 1
        for n in args:
            result *= n
    elif command == "4":
        result = 1
        for j in args:
            result /= j

    return result


print(calculator(1, 2))


# 第二种方法

def comput_exp(math_exp):
    return eval(math_exp)


print(comput_exp("2+3*4+5/5"))
