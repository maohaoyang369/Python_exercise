# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 写一个文件，里面写入从gloryroad1--gloryroad100 写入之后再读出来

with open("d:\\python\\b.txt", "w+", encoding="utf-8") as fp:
    for i in range(1, 101):
        fp.write("golord road"+str(i)+"\n")

fp = open("d:\\python\\b.txt", "r", encoding="utf-8")
data = fp.read()
fp.close()

print(data)
