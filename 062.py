#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 输出9*9口诀表

for a in range(1, 10):
    for b in range(1, a+1):
        print("%s*%s=%s" % (b, a, a*b), end=" ")
    print()




