# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 将   a = [1,2,[3,4,[5,6,7,[8,9,[10,11]]]]]  转换成  [1,2,3,4,5,6,7,8,9,10] 递归

a = [1, 2, [3, 4, [5, 6, 7, [8, 9, [10, 11]]]]]


def iter_lis_change(l):
    for i in l:
        if isinstance(i, list):
            iter_lis_change(i)
        else:
            print(i, end=" ")
    return None


iter_lis_change(a)
print(iter_lis_change(a))

# 将生成的数字放到列表中


def iter_list(l, result=[]):
    for i in l:
        if isinstance(i, list):
            iter_list(i, result)
        else:
            # print(i,end = " ")
            result.append(i)
    return result


print(iter_list(a))
