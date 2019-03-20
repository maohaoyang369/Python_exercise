# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 有一个已经排好序的列表。现输入一个数，要求按原来的规律将它插入列表中

old_list = [3, 56, 78, 102]
print(old_list)

insert_input = input("Please enter a number：")
for i in range(len(old_list)):
    if int(insert_input) < int(old_list[0]):        # 判断输入的数字小于列表中最小的数
        old_list.insert(0, int(insert_input))
        break
    elif int(insert_input) > int(old_list[len(old_list)-1]):        # 判断输入的数字大于列表中最大的数
        old_list.insert(len(old_list), int(insert_input))
        break
    elif int(insert_input) >= int(old_list[i]) and int(insert_input) <= int(old_list[i+1]):
        old_list.insert(i+1, int(insert_input))
        break

print(old_list)
