#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 打印如图所示图案，要求支持指定行数，但行数必须是奇数行


def print_pic(line):
    for i in range(1, line+1):      # 打印上半部分
        if i <= ((line + 1) / 2):       # i是上半部分的行号
            print("*  " * ((i*2)-1))

    for j in range(line, 0, -2):        # 打印下半部分
        # print(j)                      # j 是下半部分倒序的行号，每隔一行显示
        print("*  " * (2*int(j/2)-1))

print_pic(7)
