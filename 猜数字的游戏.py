#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 猜数字的游戏

import random        # 导入random模块
secret_number = random.randint(1,20)        # 定义变量secret_number为随机数字1-20
print("I am thinking of a number between 1 and 20.")        # 打印语句

# Ask the player to guess 6 times.
for guesses_taken in range(1,7):        # 循环6次
    print('Take a guess.')
    guess = int(input())        # 猜数字，input()返回一个字符串，传递给int()保存在变量guess中

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break         # 猜的数字既不大于也不小于秘密数字，跳出for循环
if guess == secret_number:
    print('Good job! You guessed my number in ' + str(guesses_taken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secret_number))