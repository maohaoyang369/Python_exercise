# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 生成一个学生资料库：
# 每个学生：名字 班级 考试成绩（科目名称，成绩）
# [名字 班级 考试成绩 [科目名称，成绩]]

# 请实现一个学生信息和成绩的录入，以及查询
# 以及更新和删除。

# 提示：每一个操作写一个函数，例如：
# add_info（）当用户输入add_info的时候，调用此函数
# 在函数内部，在实现用户输入名字和班级。

print("欢迎来到熊孩子成绩管理系统！")

print("""
可操作的命令如下：
add_info：可以添加学生的名字和班级
add_grade:可以增加学生的考试成绩
modify_grade：可以修改学生的考试成绩
get_grade:可以获得学生的某个学科考试成绩
delete_grade:可以删除学生的某个学科考试成绩
""")

xionghaizi_info = []


def add_info(info):
    if len(info) > 0:
        print("信息已存在")
        return
    name = input("请输入学生的名字：")
    info.append(name)
    class_info = input("请输入学生的班级")
    info.append(class_info)


def add_grade(info):
    if len(info) >= 3:
        subject = input("请输入学生的考试科目：")
        for i in info[2:]:
            if i[0] == subject:
                print("此学科成绩已存在")
                return
        else:
            grade = input("请输入学生此科目的考试成绩：")
            info.append([subject, grade])
    else:
        subject = input("请输入学生的考试科目：")
        grade = input("请输入学生此科目的考试成绩：")
        info.append([subject, grade])


def modify_grade(info):
    if len(info) >= 3:
        subject = input("请输入要修改的学生考试科目：")
        for i in info[2:]:
            if i[0] == subject:
                grade = input("请输入学生此科目的更改后考试成绩：")
                i[1] = grade
                return
        else:
            print("此学科的成绩不存在，无法修改：")
    else:
        print("此学生没有成绩，无须修改：")


def get_grade(info):
    if len(info) >= 3:
        subject = input("请输入要查询的学生考试科目：")
        for i in info[2:]:
            if i[0] == subject:
                print(i[1])
                return
        else:
            print("此学生无此科目成绩，无法查询!")
    else:
        print("此学生无此科目成绩，无法查询！")


def del_grade(info):
    if len(info) >= 3:
        subject = input("请输入要删除的学生考试科目:")
        for i in info[2:]:
            if i[0] == subject:
                info.remove(i)
                return
        else:
            print("此学生无此科目成绩，无法查询!")
    else:
        print("此学生无成绩可以删除!")


print("请初始化学生信息：")
add_info(xionghaizi_info)

while 1:
    command = input("请输入你的命令：")
    if command == ".":
        print("bye!")
        break
    elif command == "add_grade":
        add_grade(xionghaizi_info)
    elif command == "modify_grade":
        modify_grade(xionghaizi_info)
    elif command == "get_grade":
        get_grade(xionghaizi_info)
    elif command == "del_grade":
        del_grade(xionghaizi_info)
