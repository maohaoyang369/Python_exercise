# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 写一个类，能够实现构造函数（有参数），实现实例方法，实现类方法，实现静态方法
# 写下三个方法的调用程序


class Calculate:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):        # 实例方法
        return self.a + self.b

    @classmethod        # 类方法
    def sub(cls, c, d):
        return c-d

    @staticmethod        # 静态方法
    def mul(e, f):
        return e*f

    def div(self):
        return self.a/self.b


# 调用实例方法

c = Calculate(1, 2)
c.sum()

# 调用类方法

Calculate.sub(5, 6)

# 调用静态方法

Calculate.mul(7, 8)


class Print:

    def __init__(self, content):
        self.content = content

    def print_str(self):
        print(self.content)

    @classmethod
    def print_file(cls, file_path):
        with open(file_path) as fp:
            print(fp.read())

    @staticmethod
    def print_file_line(file_path, line_number):
        with open(file_path) as fp:
            print(fp.readlines()[line_number-1])


p = Print("hi")
p.print_str()
p.print_file("e:\\a.txt")
p.print_file_line("e:\\a.txt", 1)
