# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 实现字符串方法的类


class string_str(object):
    @classmethod
    def join(cls, arr, s):
        result = ""
        for i in arr:
            result += str(i) + s
        return result.rstrip(s)

    @classmethod
    def find(cls, s, targtet_str, start_position=0, end_position=None):
        if end_position is None:
            end_position = len(s)
        for i in range(start_position, end_position):
            if s[i:i+len(targtet_str)] == targtet_str:
                return i
        return -1

    @classmethod
    def index(cls, s, targtet_str, start_position=0, end_position=None):
        if end_position is None:
            end_position = len(s)
        for i in range(start_position, end_position):
            if s[i:i+len(targtet_str)] == targtet_str:
                return i
        return ValueError("substring not found")

    @classmethod
    def count(cls, s, target_str, start_position=0, end_position=None):
        index = start_position
        if end_position is None:
            end_position = len(s)
        times = 0
        while index < end_position-1:
            if s[index:index+len(target_str)] == target_str:
                times += 1
                # print (index)
                index += len(target_str)
            else:
                index += 1
        return times

    @classmethod
    def find_all(cls, s, target_str):
        result = []
        index = 0
        while index < len(s):
            if s[index:].find(target_str) != -1:
                result.append(index+s[index:].find(target_str))
                index += s[index:].find(target_str) + len(target_str)
            else:
                break
        return result

    @classmethod
    def split(cls, s, split_str=None, times=None):
        result = []
        positions = string_str.find_all(s, split_str)
        print(positions)
        for i in range(len(positions)):
            # print (positions[i])
            if i == 0:
                # print ("0:",positions[i])
                result.append(s[:positions[i]])
                if len(positions) == 1:
                    result.append(s[positions[i]+len(split_str):])
                if len(positions) >= 2:
                    result.append(s[positions[i]+len(split_str):positions[i+1]])
            elif i == len(positions)-1:
                # print ("1:",positions[i])
                result.append(s[positions[i]+len(split_str):])
            else:
                # print ("2:",positions[i])
                result.append(s[positions[i]+len(split_str):positions[i+1]])
        return result


print(string_str.join([1, 2, 3], "*"))
print(string_str.find("advde", "d"))
print(string_str.find("advde", "z"))
print(string_str.find("advde", "dv", 1))
print(string_str.find("advde", "dv", 1, 2))
print(string_str.index("advde", "d"))
print(string_str.index("advde", "z"))
print(string_str.count("sdfsdf", "s"))
print(string_str.count("advde", "z"))
print(string_str.count("sdfsdf", "s", 3))
print(string_str.find_all("sdfsdf", "s"))
print(string_str.find_all("advde", "z"))
print(string_str.find_all("1ab324ab3ab", "ab"))
print(string_str.split("2%t%y%", "%"))
