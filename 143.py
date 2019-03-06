# !/usr/bin/env python
# -*- coding: utf-8 -*-

# add(a,b)，要求有个值是result来存结果
# 1 a,b 数字，相加
# 2 a,b 字符串，就当做字符串相加
# 3 a,b 如果list就当list相加
# 4 不满足条件，返回None

# 第一种方法


def add(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        result = a + b
        return result
    if isinstance(a, str) and isinstance(b, str):
        result = a + b
        return result
    if isinstance(a, list) and isinstance(b, list):
        result = a + b
        return result
    else:
        return None


print(add(4, 5))
print(add("a", "b"))
print(add([1, 2, 3], [4, 5, 6]))
print(add(4, "5"))

# 第二种方法


def add(a, b):
    if isinstance(a, str) and isinstance(b, str):
        result = ""
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        result = 0
    elif isinstance(a, list) and isinstance(b, list):
        result = []
    else:
        return None
    result = a+b
    return result


print(add("1", "2"))
print(add(1, 2))
print(add([1], [2]))
print(add([1], 3))
