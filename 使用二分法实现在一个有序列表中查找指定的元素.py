#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用二分法实现在一个有序列表中查找指定的元素

sentence = [1, 22, 33, 44, 54, 55, 57, 89, 93]


def bisection_method(arr, key):
    min_num = 0
    max_num = len(arr)-1
    if key in arr:
        while True:
            center_num = int((min_num + max_num) / 2)
            if arr[center_num] > key:
                max_num = center_num - 1
            elif arr[center_num] < key:
                min_num = center_num + 1
            elif arr[]



print(bisection_method(sentence, 44))
print(bisection_method(sentence, 54))
print(bisection_method(sentence, 92))