#/usr/bin/env python
# -*- coding: utf-8 -*-!

# 编程将类似“China”这样的明文译成密文
# 密码规律是：用字母表中原来的字母后面第4个字母代替原来的字母，不能改变其大小写，
# 如果超出了字母表最后一个字母则回退到字母表中第一个字母

import string


def encrypt(sentance):
    sentance_encrypt = ""
    for i in sentance:
        # print(i)
        if i in string.ascii_letters and (ord(i)+4 >= ord('a') and ord(i)+4 <= ord('z')) \
                or (ord(i)+4 >= ord('A') and ord(i)+4 <= ord('Z')):
            i = i.replace(i, chr(ord(i) + 4))
            # print(i)
        elif i in string.punctuation or " ":
            i = i
        else:
            i = i.replace(i, chr(ord(i) - 22))
        sentance_encrypt += i
    return sentance_encrypt

print(encrypt("Hello, I am from China! 666"))