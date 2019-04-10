# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 查找指定字符串的所有位置
# 第一种方法

import re

s = "abbaaba"
result = []

for i in range(len(s)):
    if s[i:i+2] == "ab":
        result.append(i)

print(result)

# 第二种方法

s = "abbaaba"
result = []
index = 0

while 1:
    position = s.find("ab", index)
    if position != -1:
        result.append(position)
        index = position + 1
    else:
        break
print(result)

# 第三种方法：正则找出指定字符串

s = "abbaaba"

print(re.findall(r"ab", s))
