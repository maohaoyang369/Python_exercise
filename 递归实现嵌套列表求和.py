#!/usr/bin/env python
# # -*- coding: utf-8 -*-

# 递归实现嵌套列表求和

# 遍历列表的每一个元素
# 将所有元素相加，求和

array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
count = 0


def count_list_num(array):
    global count
    for i in array:
        if not isinstance(i, list):
            count += i
        else:
            count_list_num(i)
    return count


print(count_list_num(array))