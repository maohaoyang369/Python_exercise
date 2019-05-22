# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 打印分数
# 打印1/2, 1/3, 1/4,….1/10

for i in range(2, 11):
    if i <= 9:
        print("1"+"/" + str(i), end=",")
    else:
        print("1"+"/" + str(i))
