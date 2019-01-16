#/usr/bin/env python
# -*- coding: utf-8 -*-!

# 打印N，口，H图案

# N图案
import math


def print_n(height, width):
    for i in range(1, height+1):
        for j in range(1, width+1):
            if j == 1 or j == width or i == j:
                print("**", end="")
            else:
                print("  ", end="")
        print("")


print_n(5, 5)

print("''''''''''''''''''''''''''''''''''")

# 口图案


def print_square(height):
    for i in range(1, height+1):
        if i == 1 or i == height:
            print("*" * height*2)
        else:
            print("*"+" "*(height-1)*2+"*")


print_square(5)

print("''''''''''''''''''''''''''''''''''")

# H图案


def print_h(height):
    for i in range(1, height+1):
        if i == math.ceil(height/2):
            print("*"*(height+2))
        else:
            print("*"+" "*height + "*")


print_h(5)


