#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 从键盘输入两个数，并比较其大小，直到输入e/E退出程序


while True:
    a = input("Please enter number one：")
    b = input("Please enter number two: ")
    if a == "e" or a=="E" or b =="e" or b == "E":
        break
    elif a not in "01234567890eE" or b not in "01234567890eE":
        print("Please enter numbers!")
    elif int(a)>int(b):
        print(a + "大于" +b)
    elif int(a)==int(b):
        print(a + "等于" +b)
    elif int(a)<int(b):
        print(a + "小于" +b)

