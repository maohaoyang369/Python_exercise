# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 文件中有两行内容，在中间再加入一行

with open("d:\\python\\a.txt", "r+", encoding="utf-8") as fp:
    content = fp.readlines()
    content.insert(1, "gloryroad\n")
    fp.seek(0, 0)
    fp.writelines(content)
