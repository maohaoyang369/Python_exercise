#!/usr/bin/env python
# -*- coding: utf-8 -*-


def factorial_sum(num):
    count = 0
    for m in range(1, num+1):
        count_num = 1
        for i in range(1, m+1):
            count_num *= i
            # print(count_num)
        count += count_num

    return count

print(factorial_sum(4))
