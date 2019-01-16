#/usr/bin/env python
# -*- coding: utf-8 -*-!

#输出以下如下规律的矩阵
#1 2 3 4 5
#2 4 6 8 10
#3 6 9 12 15
#4 8 12 16 20

for i in range(1, 5):
    for j in range(1, 6):
        print(i*j, end='  ')
    print('')
