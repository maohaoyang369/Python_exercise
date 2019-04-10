# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 删除文件中的空行

with open("d:\\python\\a.txt", "r+") as fp:
    lines = fp.readlines()
    fp.seek(0, 0)
    for line in lines:
        if line.strip():
            fp.write(line)
