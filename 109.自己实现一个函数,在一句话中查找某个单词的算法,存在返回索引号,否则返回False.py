#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 自己实现一个函数，在一句话中查找某个单词的算法，存在返回索引号，否则返回False
# 提示：使用句子中的坐标遍历句子的每一个位置，使用查找单词的长度结合使用切片来查找单词。
# 例如：s[i:i+len(单词)]

sentence = "I am good  good good boy!"


def find_word_index(sentence, word):
    position_list = []
    word_length = len(word)
    for i in range(len(sentence)-word_length+1):
        for j in range(word_length):
            if sentence[i+j] != word[j]:
                break
        else:
            position_list.append(i)
    return position_list


print(find_word_index(sentence, "good"))
