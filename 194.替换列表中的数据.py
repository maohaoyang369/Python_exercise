# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 将[“wulaoshi”,”is”,”a”,”boy”]替换成[“wulaoshi”,”is”,”good”,”big””boy”]

sentence = ["wulaoshi", "is", "a", "boy"]

for i in range(len(sentence)):
    if sentence[i] == "a":
        sentence.remove("a")
        sentence.insert(i, "good")
        sentence.insert(i+1, "big")

print(sentence)
