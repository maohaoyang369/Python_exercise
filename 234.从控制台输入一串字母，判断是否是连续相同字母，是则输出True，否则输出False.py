# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 从控制台输入一串字母，判断是否是连续相同字母，是则输出True，否则输出False


def judge_str():
    s = input("Please enter letters: ")

    if s[0]*len(s) == s and ((s[0] >= 'a' and s[0] <= 'z') or \
    (s[0] >= 'A' and s[0] <= 'Z')):
        return True
    else:
        return False


print(judge_str())
