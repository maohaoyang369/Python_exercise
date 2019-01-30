#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 统计一句话中，一共出现了多少个单词，每个英文单词出现的次数

import pprint        # 导入pprint

message = 'I am a boy . I am a good man !'
message = message.replace('.',' ').replace('!',' ')        # 将message中的符号替换掉，就不会统计标点符号了
result = message.split()        # 将message做切片，切成每个单词
count = {}        # 定义空字典
sum = 0

for i in result:
    count.setdefault(i,0)        # 当i第一次进入字典时，值为0
    count[i] += 1        # 递增
    sum += 1
pprint.pprint(count,width=2)
print("The total number:" + str(sum))