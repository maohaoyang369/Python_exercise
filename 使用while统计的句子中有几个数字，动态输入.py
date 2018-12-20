#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用while统计的句子中有几个数字，动态输入


content = input("please input a sentence:")
result = 0
index = 0
while index <= len(content)-1:
    if content[index] in "0123456789":
        result += 1
    index += 1
print(result)