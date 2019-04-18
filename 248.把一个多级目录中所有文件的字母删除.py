#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# 把一个多级目录中所有文件的字母删除

import os
import string

file_path = []

for root, dirs, files in os.walk("d:\\python\\123"):
    for f in files:
        file_path.append(os.path.join(root, f))

print(file_path)

for f in file_path:
    filter_content = ""
    with open(f) as fp:
        content = fp.read()
        for letter in content:
            if letter in string.ascii_letters:
                continue
            else:
                filter_content += letter

    with open(f, "w") as fp:
        fp.write(filter_content)
