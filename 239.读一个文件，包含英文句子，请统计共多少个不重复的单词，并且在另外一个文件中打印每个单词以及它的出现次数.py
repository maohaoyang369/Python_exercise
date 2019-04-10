# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 读一个文件，包含英文句子，请统计共多少个不重复的单词，并且在另外一个文件中打印每个单词以及它的出现次数

# 第一步：读文件
# 方法1：open
# 方法2：with
# 难点1：怎么把英文句子中的所有标点去掉。
# 数字也要替换掉

import string

with open("d://python//a.txt", "r") as fp:
    content = ""
    for line in fp:
        s = line
        for i in string.punctuation:
            s = s.replace(i, "")
        content += s

# print(content)

word_list = content.split()
print(word_list)
print("一共%s个不重复的单词：" % len(set(word_list)))
word_count = {}
for i in word_list:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1

# print (word_count)

with open("d://python//b.txt", "w") as fp:
    fp.write("一共%s个不重复的单词：" % len(set(word_list))+"\n")
    for key, value in word_count.items():
        fp.write("%s单词出现了%s次" % (key, str(value))+"\n")
