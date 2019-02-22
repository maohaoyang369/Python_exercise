# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 实现数学中多项式求和公式的打印
# 比如：a6x^6+a5x^5+a4x^4+a3x^3+a2x^2+a1x^1+a0

polynomial = ""

for i in range(0, 7):
    if i == 0:
        polynomial = "a0"
        continue
    polynomial = "a" + str(i) + "x^" + str(i) + "+" + polynomial

print(polynomial)
