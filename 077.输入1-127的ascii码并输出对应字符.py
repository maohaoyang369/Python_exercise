#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入1-127的ascii码并输出对应字符

asc_num = input("请输入ASCII码(1-127)：")

if 1 <= int(asc_num) <= 127:
    print(chr(int(asc_num)))
else:
    print("请输入正确的ASCII码！")