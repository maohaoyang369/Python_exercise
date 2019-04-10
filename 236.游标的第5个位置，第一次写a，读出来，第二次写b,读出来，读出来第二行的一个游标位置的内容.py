# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 游标的第5个位置，第一次写a，读出来，第二次写b,读出来，读出来第二行的一个游标位置的内容

with open("d:\\python\\a.txt", "r+", encoding="utf-8") as fp:
    fp.seek(5, 0)
    fp.write("a")
    fp.seek(0, 0)
    print(fp.readline())
    fp.seek(5, 0)
    fp.write("b")
    fp.seek(0, 0)
    print(fp.readline())
    print(fp.read(1))
