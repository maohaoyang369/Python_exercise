#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 计算从0加到100的总和

total = 0
for num in range(101):        # 将0-100分别赋给变量num，执行子句
    total = total + num        # 执行100次，当循环完成 100 次迭代时，0 到 100 的每个整数都加给了 total
print(total)
