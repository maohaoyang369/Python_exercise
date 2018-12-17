#/usr/bin/env python
# -*- coding: utf-8 -*-!

# 打印100以内的素数（除了1和它本身以外不再有其他因数）


def is_prime(num):
    if not isinstance(num, int):        # 判断是否是数字
        return False
    for i in range(2, num):
        if num % i == 0:        # 如果余数为0，还有其他因数存在
            return False
    return True


for i in range(2, 101):
    if is_prime(i):
        print(i, end=" ")

