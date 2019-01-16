#!/usr/bin/env python
# # -*- coding: utf-8 -*-

# 不区分大小写对包含多个字符串对象的列表进行排序，显示排序后的结果还需要显示大小写不变的原字符串


def sort_list(list_a):
    return sorted(list_a, key=str.lower)


print(sort_list(["Opa", "A", "bre", "C", "ejk"]))
