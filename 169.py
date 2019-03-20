# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 随机生成一个1-10的整数，然后你输入一个值去比对，如果大了，打印大了，小了打印小了，等于则打印,
# 限定猜的次数不超过3次，一共猜了多少次

import random

num = random.randint(1, 10)


def is_num(n):        # 定义函数  判断是不是数字
    for i in n:
        if i not in "0123456789":
            return False
    return True


count = 0

for i in range(3):
    guess = input("Please enter number：")
    count += 1
    if not is_num(guess):
        print("Please enter right number!")
        break
    elif int(guess) > num:
        print("大了")
    elif int(guess) < num:
        print("小了")
    elif int(guess) == num:
        print("猜对了 ", guess)
        break

print("随机数字为：", num)
print("一共猜了几次：", count)
