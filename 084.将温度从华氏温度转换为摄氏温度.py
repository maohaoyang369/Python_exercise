#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 将温度从华氏温度转换为摄氏温度。转换公式为 C = 5 / 9 * (F - 32)

fah = input("请输入华氏温度：")
cen = 5 / 9 * (float(fah) - 32)
print("摄氏温度为："+ str(cen))