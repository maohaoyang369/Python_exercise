#!/usr/bin/env python
# -*- coding: utf-8 -*-

def liebiao(liebiao_li):        # 定义一个变量
    liebiao_li.insert(-1, 'and')        # 在列表最后一个字符前面添加and
    return ",".join(liebiao_li)        # 返回值 转换成字符串

spam = ['apples', 'bananas', 'tofu', 'cats']
print(liebiao(spam))        # 打印调用方法的返回结果