# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 将一个字符串转换为元组，字符串 a = "aAsmr3idd4bgs7Dlsf9eAF"

import string

sentence = "aAsmr3idd4bgs7Dlsf9eAF"

if isinstance(sentence, str):
    sentence = tuple(sentence)

print(sentence)

# 将一个字符串转换为字典，例如{"a":"A","s":"m"......}

sentence = "aAsmr3idd4bgs7Dlsf9eAF"
sentence_dic = {}

if isinstance(sentence, str):
    for i in range(1, len(sentence)):
        if i % 2 == 1:
            sentence_dic[sentence[i-1]] = sentence[i]

print(sentence_dic)

# s:m  没有是因为字典中key是唯一的，不能含有两个key都为s， 取最后的 s:f

# 请将 a 字符串的数字取出，并输出成一个新的字符串

sentence = "aAsmr3idd4bgs7Dlsf9eAF"
sentence_new = ""

for i in sentence:
    if i in "0123456789":
        sentence_new += i

print(sentence_new)

# 请统计 a 字符串出现的每个字母的出现次数（忽略大小写，a 与 A 是同一个字母），并输出成一个字典。 例 {'a':3,'b':1}

sentence = "aAsmr3idd4bgs7Dlsf9eAF"
sentence_count = {}

for i in sentence:
    if i in string.ascii_letters:
        i = i.lower()
        # print(i)
        sentence_count.setdefault(i, 0)
        sentence_count[i] += 1

print(sentence_count)

# 请去除 a 字符串多次出现的字母，仅留最先出现的一个,大小写不敏感

sentence = "aAsmr3idd4bgs7Dlsf9eAF"
sentence_count = ""

for i in sentence:
    if i in string.ascii_letters:
        i = i.lower()
        if i not in sentence_count:
            sentence_count += i
    else:
        sentence_count += i

print(sentence_count)

# 将所有的字符串变化为后一个字符串，比如“a”变成b，"z"变成A

sentence = "aAsmr3idd4bgs7Dlsf9eAF"
sentence_change = ""

for i in sentence:
    if i in string.ascii_letters[:26]:
        if ord(i) >= 122:
            sentence_change += chr(ord(i)-122+97)
        else:
            sentence_change += chr(ord(i)+1)
    elif i in string.ascii_letters[26:52]:
        if ord(i) >= 90:
            sentence_change += chr(ord(i)-90+65)
        else:
            sentence_change += chr(ord(i)+1)
    else:
        sentence_change += i

print(sentence_change)

# 删除最开始一个字母、最后一个字母和中间的2个字母dd

sentence_old = "aAsmr3idd4bgs7Dlsf9eAF"
sentence = list(sentence_old)

'''
删除中间的字母，如果是偶数个，就删除中间的两个

while True:
    if len(result)%2 == 1:
        result.remove(result[int((len(result)/2))])
        break
    elif len(result)%2 == 0:
        result.remove(result[int(len(result)/2)])
        continue
'''

for i in range(len(sentence)):
    # print(sentence[i])
    if "".join(sentence[i:i+2]) == "dd":
        del sentence[i]
        del sentence[i]
print(sentence)

'''
在i位置添加空值
for i in range(len(sentence)):
    if sentence[i] not in result:
        result.insert(i," ")
'''
for j in range(len(sentence)):
    if sentence[j] in string.ascii_letters:
        del sentence[j]
        break

print(sentence)

for i in range(len(sentence)-1, -1, -1):
    # print(sentence[i])
    if sentence[i] in string.ascii_letters:
        del sentence[i]
        break

print(sentence)
