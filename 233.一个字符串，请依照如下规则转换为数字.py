# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 一个字符串i am learning，请依照如下规则转换为数字abcd–5, efgh–10, ijkl–15, mnop–20, qrst–25, uvwx–30 yz–35
# 转换正确结果为：15 520 151052520152010

# 第一种方法

s = "i am learning"
result = ""

for i in s:
    if i in "abcd":
        result += "5"
    elif i in "efgh":
        result += "10"
    elif i in "ijkl":
        result += "15"
    elif i in "mnop":
        result += "20"
    elif i in "qrst":
        result += "25"
    elif i in "uvwx":
        result += "30"
    elif i in "yz":
        result += "35"

print(result)

# 第二种方法


def get_num(num):
    b = ""
    for i in num.lower():
        if i.isspace():        # 判断字符串中至少有一个字符且所有都是空格，否则返回false
            b += i
        else:
            value = (ord(i)-97)//4
            b += str(value*5+5)
    return b


a = "i am learning"
print(get_num(a))
