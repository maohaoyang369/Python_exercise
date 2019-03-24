# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 写一个函数，参数传入字符串”abc”,函数返回字符串“xyz”

letter = input("Please enter letters ：")


def judge(letter):
    if isinstance(letter, (int, float)):
        return False
    elif isinstance(letter, str):
        if letter == "abc":
            return "xyz"
        else:
            return False


print(judge(letter))
