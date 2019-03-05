# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 找到列表中第二大的数，可以用多种方法解决

# 思路1：
# 找到最大的，删除掉，再找最大的

spam = [1, 7, 9, 2, 5, 6]

max_spam = max(spam)
spam.remove(max_spam)
max_spam = max(spam)
print("The second num is : ", max_spam)

# 思路2：
# 排好序找倒数第二个

spam = [1, 7, 9, 2, 5, 6]

spam.sort()
second_spam = spam[-2]
print("The second num is : ", second_spam)

# 思路3：
# 遍历，声明两个变量，一个存最大的，一个存第二大的，然后逐一比对

spam = [1, 7, 9, 2, 5, 6]
spam1 = spam[0]
spam2 = spam[0]

for i in spam:
    if i >= spam1:
        spam2 = spam1
        spam1 = i
print("The second num is : ", spam2)
