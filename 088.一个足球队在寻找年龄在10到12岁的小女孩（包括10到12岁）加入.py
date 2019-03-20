#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 一个足球队在寻找年龄在10到12岁的小女孩（包括10到12岁）加入。编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。

count = 0
for i in range(1,11):
    age = input("What's your age: ")
    sex = input("What's your sex: ")
    if 10 <= int(age) <= 12 and sex == "f":
        print("You can join us!")
        count += 1
    else:
        print("Sorry, you can't join us!")   
   
print("There are "+ str(count) + " clildren can join us!")