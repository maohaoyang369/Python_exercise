# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 遍历一个列表中的嵌套列表和元组的所有元素,将1-12的数字进行输出

l = [[[1, 2, 3], 4, 5], 7, 8, (9, 10, (11, 12))]

for item in l:
    if isinstance(item, (list, tuple)):
        for i in item:
            if isinstance(i, (list, tuple)):
                for j in i:
                    print(j)
            else:
                print(i)
    else:
        print(item)
