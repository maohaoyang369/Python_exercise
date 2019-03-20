#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用二分法实现在一个有序列表中查找指定的元素

sentence = [1, 22, 33, 44, 54, 55, 57, 89, 93]


def bisection_method(arr, key):
    min_num = arr[0]
    max_num = arr[-1]
    center_num = int((min_num+max_num)/2)
    if key == center_num:
        return int(len(arr)/2)
    if key < center_num:
        return bisection_method(arr[0, int(len(arr)/2)])
    if key > center_num:
        return bisection_method(arr[int(len(arr)/2), -1])


# print(bisection_method(sentence, 44))
print(bisection_method(sentence, 54))
# print(bisection_method(sentence, 92))