# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 生成目录和文件的绝对路径

import os
import os.path


def get_dir_abs_dirpath(dir_path):        # 生成目录的绝对路径
    result = []
    for root, dirs, files in os.walk(dir_path):
        for i in dirs:
            result.append(os.path.join(root, i))
    return result


def get_dir_abs_filepath(dir_path):        # 生成文件的绝对路径
    result = []
    for root, dirs, files in os.walk(dir_path):
        for i in files:
            result.append(os.path.join(root, i))
    return result


print(get_dir_abs_dirpath("d:\\python\\123"))
print(get_dir_abs_filepath("d:\\python\\123"))
