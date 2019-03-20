# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用 for 的方式，求一下100以内奇数之和

count_odd = 0
for i in range(1, 101):
    if i % 2 == 1:
        count_odd += i
    else:
        False
print(count_odd)
