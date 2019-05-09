# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入三个数，判断是否能构成三角形能构成三角形三边关系
# 三边都大于零；两边之和大于第三边；两边之差小于第三边

triangle_a = input("Please enter the first number: ")
triangle_b = input("Please enter the second number: ")
triangle_c = input("Please enter the third number: ")


def is_num(n):        # 定义函数  判断是不是数字
    if isinstance(n, (int, float)):
        return True
    else:
        for i in n:
            if i not in "-0123456789.":
                return False
        return True


def is_triangle(a, b, c):
    if is_num(a) and is_num(b) and is_num(c):
        if int(a) > 0 and int(b) > 0 and int(c) > 0:
            if int(a) + int(b) > int(c) and int(a)+int(c) > int(b) and int(b)+int(c) > int(a):
                if int(a)-int(b) < int(c) and int(a)-int(c) < int(b) and int(b)-int(a) < int(c) and int(c)-int(a) < int(b) \
                and int(b)-int(c) < int(a) and int(c)-int(b) < int(a):
                    return "is triangle!"
                else:
                    return "is not triangle!"
            else:
                return "is not triangle!!!"
        else:
            return "Please enter integer!"
    else:
        return "please enter numbers!"


print(is_triangle(triangle_a, triangle_b, triangle_c))