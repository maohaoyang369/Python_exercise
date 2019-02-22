# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 生成9位数字和字母的密码

import string
import random
letters_num = random.randint(1, 8)
numbers_num = 9-letters_num
pass_wd = ""

for i in range(letters_num):
    pass_wd += string.ascii_letters[random.randint(0, 52)]

for i in range(numbers_num):
    pass_wd += "0123456789"[random.randint(0, 9)]

print(pass_wd)
