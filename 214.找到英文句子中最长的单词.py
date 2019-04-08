# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 找到英文句子中最长的单词 s = "I am a boy! hi , glory road"

# 算法1：
# 1 使用空格分割，列表
# 2 遍历列表，每个词
# 3 max_length =0
# 4 max_word =""

s = "I am a boy! hi , glory road  hello"
max_length = 0
max_word = []
word_list = s.split()

for word in word_list:
    if len(word) > max_length:
        max_length = len(word)
        max_word = [word]
    elif len(word) == max_length:
        max_word.append(word)

print(max_word)

# 算法2：
# 1 使用空格分割，列表
# 2 写一个函数，算出每个单词的长度
# 3 使用sort基于每个单词的长度进行排序
# 4 切片取最后一个

s = "I am a boy! hi , glory road"
s = s.split()


def letter_len(a):
    return len(a)


s.sort(key=letter_len)

print(s[-1])


s = "I am a boy! hi , glory road  hello"
word_list = s.split()
word_list.sort(key=lambda x:len(x))

for word in word_list:
    if len(word) == len(word_list[-1]):
        print(word)
