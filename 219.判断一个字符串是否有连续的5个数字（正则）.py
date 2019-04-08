# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 判断一个字符串是否有连续的5个数字（正则）

import re

s = "123kjlk12345567899"

if re.search(r"\d{5}", s):
    print("有5个连续的数字")
else:
    print("没有5个连续的数字")
