# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 将"gloryroad"按照如下规则进行加密：
# 字母对应的asscii码值进行加密，并且在码值前面加上码值长度
# 如g对应的码值为ord("g")=103，则字母g加密结果为3103
# 3是ascii的长度。
# “gloryroad”正确输出加密结果为：
# "31033108311131143121311431112973100"


def ascii_secrect(s):
    result = ""
    for i in s:
        result += str(len(str(ord(i))))+str(ord(i))

    return result


print(ascii_secrect("gloryroad"))

# 将上题中的加密字符串进行解密
# 方法有2种：
# 方法：1 种用while循环，观察加密后的规律，想办法遍历所有的内容
# 方法2： 递归实现


def decode_str(s):
    index = 0       # 每个字母的ascii码的长度
    decoded_str = ""
    while index < len(s):
        decoded_str += chr(int(s[(index+1):(index+int(s[index])+1)]))
        index = index+int(s[index])+1
    return decoded_str


print(decode_str("31033108311131143121311431112973100"))
