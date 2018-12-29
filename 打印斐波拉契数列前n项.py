#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 打印斐波那契数列前n项 (1 1 2 3 5 8 13 21 34 55....)

# 规律：除第一项和第二项以外，后面的每一项都是前两项的和
# 定义空列表
# 第一项和第二项分别打印
# 从第三项开始，每一项是前两项的和


def fib(n):
    result = []
    if n <= 0 or not isinstance(n, int):
        return result
    for i in range(n):
        if i < 2:
            result.append(1)
        else:
            result.append(result[i-1]+result[i-2])
    return result


print(fib(15))
