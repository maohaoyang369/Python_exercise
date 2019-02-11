#!/usr/bin/env python
# -*- coding: utf-8 -*-!

# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和

count = 0
a = 2
b = 1

for i in range(20):

    # print(a / b)
    count += (a/b)
    temp = a
    a = a + b
    b = temp
    # print(a, b)

print(count)

