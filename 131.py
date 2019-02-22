# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 字符串替换
# 1）读入一个字符串
# 2）去掉字符串的前后空格
# 3）如果字符串包含数字则1替换成a，2替换成b，3替换成c，以此类推
# 4）将字符串使用空格进行切分，存到一个列表，然后使用*号连接，并输出
# 5）把这些功能封装到一个函数里面，把执行结果作为返回值

import string


def replace_str(sentence):
    # result = ""
    result = sentence.strip()       # 去掉字符串前后空格
    for i in result:
        # print(i)
        if i in string.digits:      # 如果是数字替换成字符
            j = chr(ord(i) + 48)
            # print(j)
            result = result.replace(i, j)
    result = "*".join(result)       # 用*号连接
    return result.split()       # 存到列表中


sentence = input("Please enter sentence: ")
print(replace_str(sentence))
