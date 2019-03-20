# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用必填参数、默认参数、可变元组参数、可变字典参数，计算一下单词的长度之和


def sentance(a, b="qwe", *arg, **kw):
    count = 0
    count += len(a)
    count += len(b)
    for i in arg:
        count += len(i)
    for j in kw.values():
        count += len(j)
    return count


print(sentance(a="1", b="25677", c="3"))

print(sentance("a", "b", "c", "d", "e", x="f", y="g"))
# "a"赋值给参数a了，"b"给参数b了，cde给arg，x和y给kw做key f和g作为kw的value
print(sentance("a"))
print(sentance("a", c="x"))