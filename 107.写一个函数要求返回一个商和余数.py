#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 写一个函数 要求返回一个商和余数


def divmod_new(a, b):
    c = a//b
    d = a % b
    return c, d


print(divmod_new(1, 2))