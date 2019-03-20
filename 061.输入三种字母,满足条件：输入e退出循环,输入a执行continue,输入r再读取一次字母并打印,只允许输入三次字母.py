#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入三种字母，满足条件：输入e退出循环，输入a 执行continue，输入r再读取一次字母并打印，只允许输入三次字母

n = 3
while n >= 1:
    letter = input("请输入字母:")
    n -=1
    if letter == "e":
        break
    elif letter == "a":
        continue
    elif letter == "r":
        letter = input("请输入字母:")
        print(letter)