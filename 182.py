# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 生成随机的10个整数，进行求和

import random

result = 0

for i in range(10):
    num = random.randint(0, 10)
    print(num)
    result += num

print("求和为：", result)
