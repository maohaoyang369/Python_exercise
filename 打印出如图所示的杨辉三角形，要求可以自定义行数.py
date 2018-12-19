#!/usr/bin/env python
# -*- coding: utf-8 -*-m

# 打印出如图所示的杨辉三角形，要求可以自定义行数

def triangle_yanghui(line):
    for i in range(1, line+1):
        for j in range(1, line+1):
            if j == 1:
                print("  "*(line-i)+"1")
            elif j == i:
                print(j)
                print("1")
            #elif j == 2:
              #  print(" "*(2*line-i)+str(i))




print(triangle_yanghui(7))