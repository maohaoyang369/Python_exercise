#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 随机生成一个整数，1-100之间
# 你最多猜5次，如果猜大了，提示大了
# 小了，提示小了
# 猜对了，提示猜中
# 5次都没猜中，就猜没猜中

import random
number = random.randint(1, 100)

for i in range(5):
    guess = int(input("Take a guess："))
    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        break
if guess == number:
    print("Good job!")
else:
    print("Time is out")
