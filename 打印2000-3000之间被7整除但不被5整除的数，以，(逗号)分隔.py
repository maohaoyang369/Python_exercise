#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 打印2000-3000之间被7整除但不被5整除的数，以，(逗号)分隔

def num_senven():
    for i in range(2000,3001):
        if i % 7 == 0 and i % 5 != 0:
            print(i)
    return i

print(num_senven())