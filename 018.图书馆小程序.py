#!/usr/bin/env python
# -*- coding: utf-8 -*-!

# 用类实现一个图书馆，实现借书，
# 入库，还书，查书，等功能，
# 要求数据可以保存到文件中，退出后下次可以找回数据

import traceback
import pickle
import os
import os.path


class Book(object):
    def __init__(self, name, author, tag, price):
        self.__name = name
        self.__author = author
        self.__tag = tag
        self.__price = price

    def get_book_name(self):
        return self.__name

    def set_book_name(self, new_name):
        self.__name = new_name

    def book_info(self):
        print(self.name, self.author, self.tag, self.price)


class Library(object):
    '''图书馆！'''

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.book_list = []

    def get_library_info(self):
        info = "名字：%s  \n地点：%s" % (self.name, self.location)
        return info

    def add(self, book):
        self.book_list.append(book)
        print("%s图书入库成功" % book.get_book_name())

    def list(self):
        for book in self.book_list:
            print(book.get_book_name())

    def find(self):
        book_name = input("请输入要查找输的名字：").strip()
        for book in self.book_list:
            if book_name == book.get_book_name():
                print("找到%s了！" % book_name)
                break
            else:
                print("没找到%s！" % book_name)


def list_info():
    print("""
        图书馆可以输入如下命令进行操作：
        create:创建图书馆
        use：使用某个图书馆
        add:增加图书
        borrow:借阅图书
        lend:还书
        list:查看库中的图书列表
        find:查看库中是否存在某本书
        exit：退出
        """)

library = None


def create():
    global library
    library_name = input("请输入图书馆的名字：").strip()
    location = input("请输入图书馆的地址：").strip()
    library = Library(library_name, location)


def add():
    book_name = input("请输入书名：").strip()
    author_name = input("请输入作者名：").strip()
    tag = input("请输入书的分类：").strip()
    price = input("请输入书的价格：").strip()
    book = Book(book_name, author_name, tag, price)
    if library is not None:
        library.add(book)
        print("%s 图书入库成功" % book_name)
    else:
        print("图书馆还未创建，请输入create进行创建！")


def list_book():
    if library is not None:
        library.list()


library_data_file_path = ""


def use():
    global library
    global data_file_path
    data_file_path = input("请输入图书馆数据文件的位置：").strip()
    if os.path.exists(data_file_path):
        try:
            fp = open(data_file_path, "rb")
            library = pickle.load(fp)
            library_data_file_path = data_file_path
        except:
            print("图书馆的数据文件没有合法的数据！")


def find():
    global library
    if library is not None:
        library.find()


command = {"create": "create", "add": "add",
           "list": "list_book", "use": "use", "find": "find"}

if __name__ == "__main__":
    print(list_info())
    while True:
        try:
            user_command = input("请输入操作命令：").lower().strip()
            if user_command == "exit":
                if library_data_file_path == "":
                    library_data_file_path = input("请输入保存图书馆数据的数据文件路径：")
                fp = open(library_data_file_path, "wb")
                if library is not None:
                    pickle.dump(library, fp)
                fp.close()
                break
            eval(command[user_command] + "()")
        except:
            traceback.print_exc()
            if user_command not in command:
                print("您输入命令不存在!")
            else:
                print("您输入的命令有误，请按照命令列表输入：")
                print(list_info())
            continue
