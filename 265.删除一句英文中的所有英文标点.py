# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 删除一句英文中的所有英文标点

import string

sentance = "This is monica.yang@%^.。。。。"

for i in sentance:
    if i in string.punctuation:
        sentance = sentance.replace(i, "")

print(sentance)