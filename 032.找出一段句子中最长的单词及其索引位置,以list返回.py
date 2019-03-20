#!/usr/bin/env python
# -*- coding: utf-8 -*-m

# 找出一段句子中最长的单词及其索引位置，以list返回

# 1. 去除句子中的标点符号
# 2. 将句子分割成每个单词
# 3. 计算每个单词的长度
# 4. 取出最长的单词
# 5. 取出最长单词的索引位置

import string


def sentance_length(sentance):
    delete_punctuation = ""
    for i in sentance:
        if i not in string.punctuation:          # 去除句子中的标点符号
            delete_punctuation += i
    # print(delete_punctuation)
    s = delete_punctuation.split()              # 将句子分割成每个单词
    sentance_list = []
    for j in s:
        sentance_list.append(j)
    len_compare = 0
    result = []
    for n in sentance_list:                     # 求单词的长度，并将最长的单词统计出来
        if len(n) > len_compare:
            len_compare = len(n)
            result =[n]
        elif len(n) == len_compare:
            result.append(n)
    coord = []
    for m in range(len(sentance_list)):         # 查找最长单词的索引位置
        for k in result:
            if k == sentance_list[m]:
                coord.append(m)

    return result, coord


sentance = "There are many people in the office."

print(sentance_length(sentance))
