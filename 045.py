#!/usr/bin/env python
# -*- coding: utf-8 -*-!

# 等边三角形（实心）

for i in range( 5):
    print("* " * i)

# 等边三角形（空心）

print("* ")
for i in range(1, 4):
    print("*" + "  "*i + "*")
    if i == 3:
        print("*  "*4)

# 等腰三角形（实心）

for i in range(6):
    print("*" * i)

# 等腰三角形（空心）

print("*")
for i in range(6):
    print("*" + "  "*i + "*")
    if i == 5:
        print("* " * 7)

