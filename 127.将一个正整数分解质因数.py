# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 将一个正整数分解质因数，例如您输入90，分解打印90=2*3*3*5


def decompound(n):
    n = int(n)
    for i in range(2, int(n/2)+1):      # 取质数进行整除
        if n % i == 0:
            print(i, end="")
            print("*", end="")
            return decompound(n/i)
    print(n, end="")


if __name__ == "__main__":
    decompound(55)
