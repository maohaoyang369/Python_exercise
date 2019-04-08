# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 正则练习
# 给定字符串 s="i Am a gOod boy  baby!!"
# 1、判断一个字符串中字母是否全部为小写

import re
import string
import random

s = "i Am a gOod boy  baby!!"
# s = "erty6789uiodfghjk"
a = ""

for i in s:
    if i not in string.punctuation:
        a += i

if re.findall(r"[A-Z0-9]+", a):
    print("不全是小写字母")
else:
    print("全是小写")

# print(re.findall(r"[A-Z0-9]+", a))

# 2、判断有多少个空格  内部

s = "i Am a gOod boy  baby!!"
# s = "erty6789uiodfghjk"
a = ""
result = 0

if re.findall(r"\s+", s):
    result = len(re.findall(r"\s+", s))

# print(re.findall(r"\s+", a))
print("一共有 "+str(result) + " 个空格")

# 3、求大写字母的个数

s = "i Am a gOod boy  baby!!"
# s = "erty6789uiodfghjk"
a = ""
result = 0

for i in s:
    if i not in string.punctuation:
        a += i

result = len(re.findall(r"[A-Z]+", a))

# print(re.findall(r"[A-Z]+", a))
print("一共有 "+str(result) + " 个大写字母")

# 4、匹配小写字母开头的单词，计算数量

s = "i Am a gOod boy  baby!!"
# s = "erty6789uiodfghjk"
result = 0

for i in s.split():
    if re.match(r"[a-z]+", i):
        # print(i)
        result += 1

print("一共有 "+str(result) + " 个小写字母开头的单词")

# 5、查找所有单词


s = "i Am a gOod boy  baby!!"
# s = "erty6789uiodfghjk"
a = ""

for i in s:
    if i not in string.punctuation:
        a += i

print(re.findall(r"[a-zA-Z]+", a))

# 6、匹配以b开头的单词

s = "i Am a gOod boy  baby!!"
# s = "erty6789uiodfghjk"
a = ""
result = []

for i in s:
    if i not in string.punctuation:
        a += i

for i in a.split():
    if re.match(r"[b]+", i):
        result.append(i)

print(result)

# 匹配s='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'中的邮箱

s = '123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
result = []

for i in s.split(".com"):
    if not re.findall(r"[.com]+", i):
        result.append(i+".com")
        for j in result:
            if not re.findall(r"[@]+", j):
                result.remove(j)

print(result)

# 8、匹配浮点数，如“8.256”

s = '123@qq.com,687.33098,789,faSDFGHJ33333@adfcom'

print(re.findall(r"\d+[.]\d+", s))

# 9、匹配时间格式“xx年-xx月-xx日”

s = '326445sfsdf-ddas-3e,wrwe2019年-7月-11日\n,2087年-8月-65日'

print(re.findall(r'\d{4}年-\d{1,2}月-\d{1,2}日', s))

# 10、匹配s="f2sf f3sf r4re pp34f p2op" 匹配出单词，并且匹配出第二位为2的单词

s = "f2sf f3sf r4re pp34f p2op"

print(re.findall(r'[A-Za-z]+', s))

# 11、匹配hi开头的单词，只需要匹配一次。s='hi ,his name is history!'

s = 'hi,his name is history!'

s = re.sub("[,!]", " ", s)

print(re.search(r"\bhi\S*", s).group())

# 12、匹配hi开头的单词，需要匹配二次。s='hi ,his name is history!'

s = 'hi,his name is history!'

s = re.sub("[,!]", " ", s)

r = re.findall(r"\bhi\S*", s)

print(r[0:2])

# 13、匹配hi开头的单词，需要返回全部匹配结果。s='hi ,his name is history!'

s = 'hi,his name is history!'

s = re.sub("[,!]", " ", s)

print(re.findall(r"\bhi\S*", s))

# 14、匹配以ing或者noon为结尾的单词。s='good morning,good afternoon,good evening'

s = 'good morning,good afternoon,good evening'

s = re.sub("[,]", " ", s)

print(re.findall(r"\S*ing\b|\S*noon\b", s))

# 15、匹配包含tom的内容（忽略大小写）并返回匹配的个数。s='My name is Tom, and you can call me Tommy too'

s = 'My name is Tom, and you can call me Tommy too'

s = re.sub("[,]", " ", s)

print(re.findall(r"\S*tom\S*", s, re.I))
print(len(re.findall(r"\S*tom\S*", s, re.I)))

# 16、匹配以in开头单词的后半部分（如integrated-->返回tegrated）。s='introduction,i am interesting boy'

s = 'introduction,i am interesting boy'

s = re.sub("[,]", " ", s)

print(re.findall(r"\bin(\S*)", s))

# 17、匹配不包含连续字符串abc的单词。s='abcddd qweabee ddabc abc cba'

s = 'abcddd qweabee ddabc abc cba'
# s = re.sub("[,]"," ",s)
result = []

m = re.findall(r"[a-zA_Z]*abc[a-zA_Z]*", s)

print(m)

for i in s.split():
    if i not in m:
        result.append(i)

print(result)

# 18、匹配网址格式，如www.baidu.com或者https://www.baidu.com/

s = 'www.baidu.com,https://www.baidu.com/,35676788,567jklk.987j'

print(re.findall(r"[a-zA-z]+://[^\s]*.com|[^\s]*.com|[a-zA-z]+://[^\s]*.cn|[^\s]*.com", s))

# 19、匹配指定格式的电话号码，如010-1234-5678或者1234-5678

s = '123-45677,35676788,asda-huyi,010-1234-5678,1234-5678'

print(re.findall(r"\d{3}-\d{4}-\d{4}|\d{4}-\d{4}", s))

# 20、随机生成10位数字，如果10位数字中有任意3位连续数字，返回666，否则返回0

s = random.randint(1000000000, 9999999999)

print(s)

if re.search(r"(\d)\1\1", str(s)):
    print("666")
else:
    print("0")
