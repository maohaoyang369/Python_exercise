#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 要求实现一函数，该函数用于求两个集合的差集，结果集合中包含所有属于第一个集合但不属于第二个集合的元素

def set_sub(set_a, set_b):
    set_sub_result = set()
    for i in set_a:
        set_sub_result.add(i)
        for j in set_b:
            if i == j:
                set_sub_result.remove(i)

    return set_sub_result

print(set_sub(("1","2","3"),("1","4","5","6")))


