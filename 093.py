#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  实现一个简单的单词本，
# 功能：可以添加单词和词义，当所添加的单词已存在，让用户知道
# 可以查找单词，当查找的单词不存在时，让用户知道
# 可以删除单词，当删除的单词不存在时，让用户知道
# 以上功能可以无限制操作，直到用户输入bye退出程序

word_book = {}

while True:
    name = input("Enter a book：")
    if name == '':
        break
    if name in word_book:
        print(name,"：", word_book[name])
        del_key = input("Do you want delete it? Please enter Y or N：")
        if del_key == "Y":
            del word_book[name]
        else:
            continue
    else:
        print("You don't have this word, please enter the meaning：")
        meaning = input()
        word_book[name] = meaning
        print("Your word book is update!")