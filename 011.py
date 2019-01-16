#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用一个列表，可以保存用户输入的任意多的猫

cat_names = []        # 定义一个变量
while True:
    print("Enter the name of cat " + str(len(cat_names) + 1) + " (Or enter nothing to stop):")
    name = input()        # 输入猫的名字
    if name == "":        # 当输入的字符为空时，跳出循环
        break
    cat_names = cat_names + [name]        # 每增加一只猫，向列表中添加
print("The cat names are:")
for name in cat_names:        # 遍历列表中的猫
    print(''+ name)