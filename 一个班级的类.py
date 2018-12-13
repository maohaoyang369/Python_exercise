#/usr/bin/env python
# -*- coding: utf-8 -*-!


class Student(object):

    def __init__(self, name, grade_class_no):
        self.name = name
        self.grade_class_no = grade_class_no
        self.__chinese_score = None
        self.__math_score = None
        self.__english_score = None

    def set_chinese_score(self, score):

        if score >= 0 and score <= 100 and isinstance(score, (int, float)):
            self.__chinese_score = score
        else:
            print("你输入的分数不是数字类型，或者不在0-100分数的范围内！")

    def get_chinese_score(self):
        return self.__chinese_score

    def set_math_score(self, score):

        if score >= 0 and score <= 100 and isinstance(score, (int, float)):
            self.__math_score = score
        else:
            print("你输入的分数不是数字类型，或者不在0-100分数的范围内！")

    def get_math_score(self):
        return self.__math_score

    def set_english_score(self, score):

        if score >= 0 and score <= 100 and isinstance(score, (int, float)):
            self.__english_score = score
        else:
            print("你输入的分数不是数字类型，或者不在0-100分数的范围内！")

    def get_english_score(self):
        return self.__english_score

    def get_max_score(self):
        return max(self.__chinese_score, self.__math_score, self.__english_score)

    def get_avg_score(self):
        return sum([self.__chinese_score, self.__math_score, self.__english_score]) / 3

    def get_total_score(self):
        return sum([self.__chinese_score, self.__math_score, self.__english_score])


class Class_NO(object):

    """管理班级数据的类"""

    def __init__(self, name):
        self.grade_class_name = name
        self.students = []

    def set_grade_class_name(self, name):
        self.grade_class_name = name

    def get_grade_class_name(self):
        return self.grade_class_name

    def add_student(self, student):
        self.students.append(student)

    def get_max_total_score(self):
        student_total_score = []
        for i in self.students:
            student_total_score.append(i.get_total_score())
        return max(student_total_score)

    def get_avg_score(self):
        student_total_score = []
        for i in self.students:
            student_total_score.append(i.get_total_score())
        return sum(student_total_score) / len(self.students)


if __name__ == "__main__":
    s = Student("张三", "三年级二班")
    s.set_chinese_score(100)
    s.set_math_score(80)
    s.set_english_score(60)
    t = Student("李四", "三年级二班")
    t.set_chinese_score(100)
    t.set_math_score(50)
    t.set_english_score(10)
    c = Class_NO("三年级二班")
    c.add_student(s)
    c.add_student(t)
    print(c.get_max_total_score())
    print(c.get_avg_score())