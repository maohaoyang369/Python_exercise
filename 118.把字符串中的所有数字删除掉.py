# !/usr/bin/env python
# -*- coding: utf-8 -*

# 把字符串中的所有数字删除掉

a = "a1b2c3b4d5"
b = []
for i in a:
    if i not in "0123456789":
        b.append(i)
print("".join(b))
