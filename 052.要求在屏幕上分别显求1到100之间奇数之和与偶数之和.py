#!/usr/bin/env python
# -*- coding: utf-8 -*-

num = 0
ou_num = 0

for i in range(101):
    if i % 2 == 0:
        ou_num += i
    else:
        num += i

print(ou_num)
print(num)
