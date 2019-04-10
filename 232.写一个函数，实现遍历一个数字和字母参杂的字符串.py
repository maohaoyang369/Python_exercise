# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 写一个函数，实现遍历一个数字和字母参杂的字符串，如果碰到字母则替换成*，
# 最后*隔开的数字作为整体计算求和。
# 如”ab34aa243dd78eww89”，则替换成*的结果为：”**34**243**78***89”，求和结果为：”***7**9**15***17”

# 第一种方法

import re

s = "ab34aa243dd78eww89"
result = ""
count = 0
flag = False

for i in s:
    if i >= 'a' and i <= "z":
        if flag == True:
            result += str(count)
            flag = False
            count = 0
        result += "*"
    else:
        flag = True
        count += int(i)

if count != 0:
    result += str(count)

print(result)

# 第二种方法

s = "ab34aa243dd78eww89"
result = ""
s = re.sub(r"[a-z]", "*", s)
arr1 = re.split("\\*+", s)     # ['', '34', '243', '78', '89']

for i in range(len(arr1)):
    count = 0
    if arr1[i].isdigit():
        for j in arr1[i]:
            count += int(j)
    if count != 0:
        arr1[i] = str(count)

arr2 = re.split("\\d+", s)        # ['**', '**', '**', '***', '']

for i in range(len(arr1)):
    result += arr1[i]+arr2[i]

print(result)
