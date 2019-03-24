# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 求两个数的最大公约数（递归）

# 第一种方法


def greatest_common_divisor(a, b, c=0, result=[]):
    if c == 0:        # 定义默认的c 判断a和b的大小，取小的值赋给c
        if a < b:
            c = a
        else:
            c = b
    if a % c == 0 and b % c == 0:
        result.append(c)
    else:
        greatest_common_divisor(a, b, c-1)

    return result[-1]


print(greatest_common_divisor(10, 8))
print(greatest_common_divisor(10, 5))

# 第二种方法 更相减损法


def get(small, big):
    if small > big:
        small, big = big, small
    if small == big:
        return small
    return get(small, big - small)


print(get(10, 8))
print(get(10, 5))

# 第三种方法 辗转相除法


def gain(small, big):
    if small > big:
        small, big = big, small
    if small == 0:
        return big
    return gain(small, big % small)


print(gain(10, 8))
print(gain(10, 5))
