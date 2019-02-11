#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 设定一个用户名和密码，用户输入正确的用户名和密码，则显示登录成功，否则提示登录失败，用户最多失败3次，否则退出程序
# 提示：使用while或者for来限定重试的次数，使用input获取用户输入使用 ==判断用户的用户名和密码

user_password = {'11':11,'root':12}

for i in range(3):
    user1 = input("请输入用户名：")
    password = input("请输入密码：")
    if user1 in user_password and user_password[user1] == int(password):
        print("登录成功")
        break
    else:
        print("请输入正确的用户名和密码")
if i == 3:
    print("次数用完了")

# while的解决方法

user_name_in_system = "root"
user_passwd_in_system = "root123"
i = 2
while i >= 0:
    user_name_input = input("please input username:")
    user_passwd_input = input("please input passwd:")
    if user_name_input == user_name_in_system and \
       user_passwd_input == user_passwd_in_system:
        print("login successfully!")
        break
    else:
        print("wrong username or password!")
        if i == 0:
            print("input times is used out! bye!")
        i -= 1