# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 统计列表中  字符串出现了几次    L = [1,2,"s",[1,23],{1:2},(1,2),set([1,2]),"b"]

L = [1, 2, "s", [1, 23], {1: 2}, (1, 2), set([1, 2]), "b"]
count = 0
for i in L:
    if isinstance(i, str):
        count += 1

print(count)

# 将所有的数据类型都统计一遍 放到字典里面

L = [1, 2, "s", [1, 23], {1: 2}, (1, 2), set([1, 2]), "b"]
d = {"int": 0, "str": 0, "list": 0, "tuple": 0, "set": 0, "dict": 0}
for i in L:
    if isinstance(i, str):
        d["str"] += 1
    elif isinstance(i, int):
        d["int"] += 1
    elif isinstance(i, list):
        d["list"] += 1
    elif isinstance(i, set):
        d["set"] += 1
    elif isinstance(i, tuple):
        d["tuple"] += 1
    elif isinstance(i, dict):
        d["dict"] += 1

print(d)
