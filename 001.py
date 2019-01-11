#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 写一个函数实现一个数学公式

import math


def circle_area(radius):
    circle = math.pi * radius * radius
    return circle

print(circle_area(4))
print(circle_area(1))
