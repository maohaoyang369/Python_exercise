# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 随机生成一个4位长度的整数数字，判断是否同时包含1和0

import random

spam = str(random.randint(1000, 9999))
print(spam)
if "1" in spam and "0" in spam:
    print("包含1和0")
else:
    print("不包含1和0")
