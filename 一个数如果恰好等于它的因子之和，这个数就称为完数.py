#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 一个数如果恰好等于它的因子之和，这个数就称为完数，例如6的因子为1,2,3，
# 而6=1+2+3，因此6是完数，编程找出1000之内的所有完数，并按6 its factors are 1,2,3这样的格式输出

result = []

for i in range(1, 1001):
    divisor = []
    for j in range(1, i):
        if i % j == 0:
            divisor.append(j)
    # print(divisor)
    if sum(divisor) == i:
        result.append(i)

print(result)
