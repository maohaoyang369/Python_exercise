# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用while,计算随机数之和，超过100的时候，停止程序
# 随机数1-20的范围产生，要求记录一下产生的随机数，以及最后的和，以及随机数的个数

import random

random_number = []
random_plus = 0

while True:
    number = random.randint(1, 20)
    random_number.append(number)
    random_plus += number
    if random_plus > 100:
        break

print("随机数的个数为："+str(len(random_number)))
print("随机数的总和："+str(random_plus))
print("随机数为："+str(random_number))

# 第二种方法

result = 0
random_num_list = []
while 1:
    random_num = random.randint(1, 20)
    random_num_list.append(random_num)
    result += random_num
    if result > 100:
        break

print("一共产生了 %s 个随机数：" % len(random_num_list))
print("产生随机数如下：", random_num_list)
print("最后的随机数之和：", result)
