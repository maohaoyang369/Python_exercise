#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 逗号代码  以一个列表值作为参数，返回一个字符串。该字符串包含所有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入 and。
# 例如，将前面的 spam 列表传递给函数，将返回'apples, bananas, tofu, and cats'。但你的函数应该能够处理传递给它的任何列表。

def liebiao(liebiao_li):        # 定义一个变量
    liebiao_li.insert(-1, 'and')        # 在列表最后一个字符前面添加and
    return ",".join(liebiao_li)        # 返回值 转换成字符串

spam = ['apples', 'bananas', 'tofu', 'cats']
print(liebiao(spam))        # 打印调用方法的返回结果