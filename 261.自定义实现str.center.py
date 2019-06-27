# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 自定义实现str.center(numbe) 居中

import math


def center(sentance, number):
    len_sentance = len(sentance)
    half_number = number-len_sentance
    if number <= len_sentance:
        return sentance, len(sentance)
    else:
        if number % 2 == 0 and half_number == 1:
            sentance += " " * half_number
            return sentance, len(sentance)
        else:
            print_center = (math.ceil(half_number/2) * " ") + sentance +\
                ((half_number-math.ceil(half_number/2)) * " ")
    return print_center, len(print_center)


print(center("abc", 4))
