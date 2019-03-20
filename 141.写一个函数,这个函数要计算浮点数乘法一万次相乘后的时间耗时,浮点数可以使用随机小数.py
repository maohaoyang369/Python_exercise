# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 写一个函数，这个函数要计算 浮点数乘法 一万次相乘后的时间耗时，浮点数可以使用随机小数

import time
import random


def float_time(s):
    start_time = time.time()
    for i in range(s):
        result = random.random()**2
    end_time = time.time()
    return end_time-start_time


print(float_time(100000))
