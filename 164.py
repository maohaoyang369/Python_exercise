# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 生成一个随机的8位密码，要求4个字母和4个数字

import random
import string

spam_num = random.choices("0123456789", k=4)
print(spam_num)
spam_letters = random.sample(string.ascii_letters, 4)
print(spam_letters)
spam = spam_num+spam_letters
print(spam)
spam_num_letters = random.shuffle(spam)
print(spam)
secrity = "".join(spam)
print(secrity)
