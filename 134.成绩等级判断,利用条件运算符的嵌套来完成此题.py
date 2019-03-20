# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 成绩等级判断，利用条件运算符的嵌套来完成此题
# 学习成绩 >= 90分的同学用A表示
# 60-89分之间的用B表示
# 60分以下的用C表示

result = input("please enter your result : ")

for i in result:
    if i not in "0123456789":
        print("None")
    else:
        if int(result) >= 90:
            print("A")
        elif int(result) >= 60 and int(result) < 89:
            print("B")
        else:
            print("C")
    break
