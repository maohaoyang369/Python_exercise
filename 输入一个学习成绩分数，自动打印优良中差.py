#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入一个学习成绩分数，自动打印优良中差

result = input("请输入学习成绩:")

if 90 <= int(result) <= 100:
    print("优")
elif 80 <= int(result) < 90:
    print("良")
elif 70 <= int(result) < 80:
    print("中")
elif 60 <= int(result) < 70:
    print("及格")
elif 0 <= int(result) < 60:
    print("不及格")
else:
    print("Error！")