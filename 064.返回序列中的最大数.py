#!/usr/bin/env python
# -*- coding: utf-8 -*-m

# 返回序列中的最大数


def biggest_num(sentance):
    if isinstance(sentance, list):
        list_sort = sorted(sentance)
        # print(list_sort[-1])
        result = list_sort[-1]
    elif isinstance(sentance, str):
        s = sentance.split()
        s_list = []
        for i in s:
            s_list.append(i)
        # print((sorted(s_list))[-1])
        result = (sorted(s_list))[-1]
    elif isinstance(sentance, tuple):
        tuple_list = []
        for j in sentance:
            tuple_list.append(j)
        # print((sorted(tuple_list))[-1])
        result = (sorted(tuple_list))[-1]
    return result


sentance = [1, 7, 3, 4]
sentance_one = "7 900 100"
sentance_two = (1, 2, 3, 23)

print(biggest_num(sentance))
print(biggest_num(sentance_one))
print(biggest_num(sentance_two))

