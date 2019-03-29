# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 正方形

for i in range(4):
    if i == 0:
        print("*"*7)
    elif i == 3:
        print("*"*7)
    else:
        print("*     *")

# 实心三角形

for i in range(10):
    print("***"*i+"*")

# 空心三角形

print("*")
for i in range(5):
    print("*"+"  "*i+"*")
    if i == 4:
        print("*"*(i+7))

# 函数实现空心三角形


def draw_triangle(n):
    print("*")
    for i in range(n-2):
        print("*"+"   "*i+"*")
    print("*"*((n-2)*3))


draw_triangle(10)
