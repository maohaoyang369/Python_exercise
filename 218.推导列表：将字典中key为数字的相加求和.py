# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 推导列表：将字典中key为数字的相加求和

a = {1:'a', 2:'b', 'a':3}

print(sum([i for i in a.keys() if isinstance(i, int)]))

# 将字典中key 和 value 均为数字的相加求和

a = {1:'a', 2:'b', 'a':3}

print(sum([i for i in a.keys() if isinstance(i, int)]+[j for j in a.values() if isinstance(j, int)]))