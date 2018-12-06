#!/usr/bin/env python
# -*- coding: utf-8 -*-

for i in range(1001):   # 1000以内所有数字
    if len(str(i)) == 3:        # 水仙花一定是3位数
        if pow(int(str(i)[0]), 3) + pow(int(str(i)[1]), 3) + pow(int(str(i)[2]), 3) == i:       # pow() 多次方
            print(i)
