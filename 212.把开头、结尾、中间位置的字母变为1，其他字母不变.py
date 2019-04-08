# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 把开头、结尾、中间位置的字母变为1，其他字母不变 a = "abcdefghi"
# 第一种方法

a = "abcdefgh"
b = list(a)
b[0] = '1'
b[-1] = '1'

if len(b) % 2 == 1:
    b[int(len(b)/2)] = '1'
elif len(b) % 2 == 0:
    b[int(len(b)/2)] = '1'
    b.remove(b[int(len(b)/2-1)])

print("".join(b))


# 第二种方法

a = "abcdefgh"
a = list(a)
a[0] = '1'
a[-1] = '1'
mid = len(a)//2

if len(a) % 2 == 0:
    a[mid] = '1'
    a[mid-1] = '1'
else:
    a[mid] = '1'

print("".join(a))
