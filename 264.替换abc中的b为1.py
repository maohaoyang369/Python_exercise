# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 替换abc中的b为1

import re

sentance = "abc"

# 1 利用列表

sentance = list(sentance)

sentance[1] = "1"
print("".join(sentance))

# 2 直接拼接

sentance = sentance[0] + "1" + sentance[2]

print(sentance)


# 3 replace替换
sentance = sentance.replace("b", "1")
print(sentance)


# 4 利用b分割再拼接

print("1".join(sentance.split("b")))


# 5 正则sub替换

print(re.sub(r"b", "1", sentance))


# 6 删除再插入

sentance = list(sentance)

sentance.pop(1)
sentance.insert(1, "1")

print("".join(sentance))