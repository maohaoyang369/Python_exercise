# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 把‘abc’中的b替换成1  s='abc'

# 遍历

import re

s = 'abc'
s = list(s)

for i in s:
    print(i)
    if i == "b":
        s[1] = "1"

print("".join(s))

# replace

s = 'abc'

print(s.replace("b", "1"))

# 相加

s = 'abc'

print(s[0]+"1"+s[2])

# 先切后拼

s = 'abc'

print('1'.join(s.split('b')))

# 正则

s = 'abc'

print(re.sub(r'b', '1', s))
