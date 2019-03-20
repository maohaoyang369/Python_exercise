# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 写一个函数，识别输入字符串是否是符合 python 语法的变量名（不能数字开头、只能使用数字和字母以及‘_’）

import re


def py_grammer_name(sen):
    grammer_name = str(sen)
    if re.match(r"^\d", grammer_name):
        print("不能是数字开头")
        return False
    elif re.search(r"\W", grammer_name):
        print("只能使用数字和字母以及‘_’")
        return False
    else:
        return True


print(py_grammer_name("34ljsd"))
print(py_grammer_name("ljsd"))
print(py_grammer_name("lj_s435d"))
