#!/usr/bin/env python
# -*- coding: utf-8 -*-

sentance = "Please find the words"


def find_word(sentance, word):
    sentance_len = len(word)
    print(sentance_len)
    for i in range(len(sentance)):
        if sentance[i:i+sentance_len] == word:
            return sentance[i:i+sentance_len]
    return False

print(find_word(sentance, 'the'))
print(find_word(sentance, 'dound'))