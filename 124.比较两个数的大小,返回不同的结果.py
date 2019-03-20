# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 生成9位数字的密码

import random

pass_wd = ""
chr(ord("0")+random.randint(0, 9))
for i in range(9):
    pass_wd += chr(ord("0")+random.randint(0, 9))

print(pass_wd)
