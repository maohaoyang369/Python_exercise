# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 嵌套循环输出10-50中个位带有1-5的所有数字

# 方法1：数字和10取余，判断是否大于0并且小于等于5

for i in range(10, 51):
    if i % 10 > 0 and i % 10 <= 5:
        print(i)

# 方法2：将数字转换为str，取各位的字符，判断字符是否在1-5内

for m in range(10, 51):
    if str(m)[1] in "12345":
        print(m)

# 方法3：嵌套的方式来实现

for i in "1234":
    for j in "12345":
        print(int(i+j))
