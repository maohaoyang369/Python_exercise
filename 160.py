# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 判断一个字符串是否包含非数字内容

sentence = "adsfdsds,.13579"
is_break = False
for i in sentence:
    if i in "0123456789":
        is_break = True
        break
if not is_break:
    print("不包含数字")
else:
    print("包含数字")
