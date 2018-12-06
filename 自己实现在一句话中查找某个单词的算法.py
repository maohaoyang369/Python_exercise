#!/usr/bin/env python
# -*- coding: utf-8 -*-

sentance = "Please find the words."


def find_word(sentance, word):
    sentance_len = len(sentance)
    print(sentance_len)
    sentance_list = sentance.split(" ")
    print(sentance_list)
    for i in range(sentance_list):
        print(i)
        if i == word:
            return "\"\""
        else:
            return False

print(find_word(sentance, 'the'))
