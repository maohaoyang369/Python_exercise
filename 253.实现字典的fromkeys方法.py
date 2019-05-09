# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 实现字典的fromkeys方法
# 例如：
# seq = ('name', 'age', 'sex')
# dict = dict.fromkeys(seq, 10)
# print "New Dictionary : %s" % str(dict)
# 结果：New Dictionary : {'age': 10, 'name': 10, 'sex': 10}


def fromkeys_function(dic_keys, dic_values):
    form_dict = {}
    for i in dic_keys:
        form_dict[i] = dic_values
    return form_dict


dic_keys = ('name', 'age', 'sex')

print(fromkeys_function(dic_keys, 100))
