# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 把目录下所有的txt文件干掉，新建一个空的子目录xxx，放在某个层级下，,把它删掉

import os
import os.path

dir_count = 0
file_count = 0
for root, dirs, files in os.walk("d:\\python\\123", topdown=True):
    print(u"当前目录:", root)   # 打印目录绝对路径
    for name in files:
        print(u'文件名：', os.path.join(root, name))    # 打印文件绝对路径
        if name[-4:] == ".txt":
            os.remove(os.path.join(root, name))
        file_count += 1
    for name in dirs:
        print(u'目录名：', name)     # 打印目录绝对路径
        if name == "XXX":
            os.rmdir(os.path.join(root, name))
        dir_count += 1

print("目录个数%s" % dir_count)
print("文件个数%s" % file_count)
