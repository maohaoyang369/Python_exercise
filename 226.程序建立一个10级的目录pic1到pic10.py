# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 程序建立一个10级的目录pic1到pic10

import os

# root_dir = "d:\\python36"
# os.chdir("d:\\python36")

for i in range(1, 11):
    os.mkdir("pic"+str(i))
    os.chdir("pic"+str(i))
