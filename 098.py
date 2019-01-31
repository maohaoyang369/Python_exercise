#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 求两个正整数m和n的最大公约数


def common_divisor(m,n):
    if m > n:
        samller = n
    else:
        samller = m
    for i in range(1,samller + 1):
        if m % i == 0 and n % i == 0:
            common_divisor = i
    return common_divisor

    
num1 = int(input("Enter the number："))
num2 = int(input("Enter the second number："))
print("The maximum common divisor of ", num1,"and", num2, "is：",common_divisor(num1,num2))