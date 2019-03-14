# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 判断一个四位的数字，是否可以被2和5同时整除，如果可以打印可以整除，否则打印不可以整除

spam = input("Please enter numbers : ")
is_break = True

if len(spam) != 4:
    is_break = False

for i in spam:
    if i not in "0123456789":
        is_break = False
        break

if not is_break:
    print("Please enter right number!")
elif int(i) % 2 == 0 and int(i) % 5 == 0:
    print("可以整除")
else:
    print("不可以整除")
