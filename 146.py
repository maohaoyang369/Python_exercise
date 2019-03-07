# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入10个数字，算一下累加和

count = 0
for j in range(10):
    num = input("Please enter a number：")
    is_break = False
    for i in num:
        if i not in "01234567890.-":
            print("It's not number!")
            is_break = True
            break
    if is_break == True:
        count = None
        break
    count += float(num)

if count != None:
    print(count)
