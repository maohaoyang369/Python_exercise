#!/usr/bin/env python
# # -*- coding: utf-8 -*-

# 递归实现嵌套列表求和

# 遍历列表的每一个元素
# 将所有元素相加，求和

array = [[1, 2, 3], [4, 15, 6], [7, 8, 9]]


def count_list_num(array):
    count = 0
    for i in array:
        if not isinstance(i, list):
            count += i
        else:
            count += count_list_num(i)
    return count


print(count_list_num(array))
