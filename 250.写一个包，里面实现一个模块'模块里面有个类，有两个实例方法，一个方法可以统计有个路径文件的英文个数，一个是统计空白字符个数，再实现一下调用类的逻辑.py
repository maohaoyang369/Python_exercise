# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 写一个包，里面实现一个模块'模块里面有个类
# 有两个实例方法
# 一个方法可以统计有个路径文件的英文个数
# 一个是统计空白字符个数，再实现一下调用类的逻辑

import string


class Count(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def count_letter_num(self):
        letter_num = 0
        try:
            with open(self.file_path) as fp:
                for line in fp:
                    for letter in line:
                        if (letter >= "a" and letter <= "z") or \
                        (letter >= "A" and letter <= "Z"):
                            letter_num += 1
            return letter_num
        except IOError as e:
            print(e)
            return None

    def count_space_num(self):
        space_num = 0
        try:
            with open(self.file_path) as fp:
                for line in fp:
                    for letter in line:
                        if letter.isspace():
                            space_num += 1
            return space_num
        except IOError as e:
            print(e)
            return None


# 调用程序

import count.string_count   

f = count.string_count.Count("d:\\python\\a.py")
print(f.count_letter_num())
print(f.count_space_num())

# 统计一下两个句子中不重复单词数量，并列出哪些单词出现了重复值

s1 = "I am a boy,good boy!"
s2 = "I am not a boy,good girl!"

for i in string.punctuation:
    s1 = s1.replace(i, " ")
    s2 = s2.replace(i, " ")
    
word_list1 = set(s1.split())
word_list2 = set(s2.split())

result1 = word_list1-word_list2
result2 = word_list2-word_list1

result = len(list(result1 | result2))

print(result)
print(len(list(word_list1 ^ word_list2)))        # 异或