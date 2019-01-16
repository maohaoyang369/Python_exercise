#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 从键盘输入两个数，并比较其大小，直到输入e/E退出程序

while True:
    a = input("Please enter number one：")
    b = input("Please enter number two: ")
    status = 0
    for i in a:
        if i not in "01234567890eE":
            print("Please enter numbers!")
            status = 1
    for j in b:
        if j not in "01234567890eE":
            print("Please enter numbers!")
            status = 1
    if status == 1:
        break
    if a == "e" or a == "E" or b == "e" or b == "E":
        break
    elif int(a) > int(b):
        print(a + "大于" + b)
    elif int(a) == int(b):
        print(a + "等于" + b)
    elif int(a) < int(b):
        print(a + "小于" + b)

