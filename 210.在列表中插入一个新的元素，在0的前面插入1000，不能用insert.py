# !/usr/bin/env python
# -*- coding: utf-8 -*-

# a = [10, -5, -1, 2, 3, 0, 5]  在列表中插入一个新的元素，在0的前面插入1000，不能用insert

a = [10, -5, -1, 2, 3, 0, 5]
b = []

for i in range(len(a)):
    if a[i] == 0:
        b.append(1000)
        b.append(a[i])
    if a[i] != 0:
        b.append(a[i])

print(b)

# 在列表中第三个位置，插入1000

a = [10, -5, -1, 2, 3, 0, 5]
front = []
behind = []
middle = [1000]
for i in a[:3]:
    front.append(i)

for j in a[3:]:
    behind.append(j)

# print(front)
# print(behind)
print(front+middle+behind)

result = []
result = a[:3] + middle + a[3:]
print(result)
