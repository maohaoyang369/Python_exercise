# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

# 1 考英语
# s = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# 2 输入一个字符，判断是否在s的所有单词的
# 第一个字母是否存在
# 3 有，第一种只有唯一首字母匹配到了，
# 第二种2个单词的首字母匹配到了。
# 遍历：判断首字母相同的单词有几个，存个list
# 如果list长度是1，说明没有重复的天，直接输出
# 如果List长度是2，说明有2个。再让用户输入一个字母
# 判断在list的所有单词的第二个是否相等，相等就可以输出结果了。


def get_weekday():
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    first_letter = input("Please enter a letter: ")
    result = []
    for i in week:
        if first_letter.lower() == i[0].lower():
            result.append(i)
    # print(result)
    if len(result) == 0:
        return ""
    if len(result) == 1:
        return result
    if len(result) == 2:
        second_letter = input("Please enter second letter: ")
        # print(result)
        for j in result:
            # print(j)
            if j[1] == second_letter:
                return j


print(get_weekday())
