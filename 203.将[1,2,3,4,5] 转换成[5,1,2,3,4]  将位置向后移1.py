# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 将[1,2,3,4,5] 转换成[5,1,2,3,4]  将位置向后移1

# 第一种方法

a = [1, 2, 3, 4, 5]
temp = a[-1]

for i in range(len(a), 0, -1):
    a[i-1] = a[i-2]

a[0] = temp

print(a)

# 第二种方法

num = [1, 2, 3, 4, 5]
num_new = []
for i in range(0, len(num)):
    num_new.append(num[i-1])
    # print(num[i-1])

print(num_new)
