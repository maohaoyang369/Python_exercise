# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 统计一下某个目录下的，所有不同后缀名的个数，以及哪些具体的后缀名

import os
import os.path


def get_postfix_name_count(dir_path):
    result = []
    for root, dirs, files in os.walk(dir_path):
        for i in files:
            postfix_name = os.path.splitext(os.path.join(root, i))[1]
            if postfix_name != "":
                result.append(postfix_name[1:])
    return list(set(result)), len(set(result))


print(get_postfix_name_count("d:\\python"))
