#/usr/bin/env python
# -*- coding: utf-8 -*-!

# 一个字符串 list，每个元素是 1 个 ip，输出出现次数最多的 ip

sentance_list = ["a","e","r","t","y","u",6,5,4,"f","g","er","a","s","e",4,4,4,"a","a"]

sentance_count = []

times = 0

for i in sentance_list:
    # print(i)
    if sentance_list.count(i) > times:
        sentance_count = []
        sentance_count.append(i)
        times = sentance_count.count(i)
    elif sentance_list.count(i) == times:
        sentance_count.append(i)
print(sentance_count)
