#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 把一个文件中的所有数字删除

filtered_content = ""
with open("d:\\python\\a1.txt", "r") as fp:
    content = fp.read()
    for i in content:
        if i in "0123456789":
            continue
        else:
            filtered_content += i

with open("d:\\python\\a1.txt", "w") as fp:
    fp.write(filtered_content)

with open("d:\\python\\a1.txt", "r") as fp:
    print(fp.read())
