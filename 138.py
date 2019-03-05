# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 将一个文件中的所有alex字符，替换为superman

fp = open("d:\\python36\\a.txt", "r+", encoding="utf-8")
sentence = fp.readlines()
fp_new = open("d:\\python36\\a1.txt", "w", encoding="utf-8")        # 将替换后的内容写到新的文件中
for i in sentence:
    # print(i)
    if "alex" in i:
        i = i.replace("alex", "superman")
        # print(i)
    else:
        pass
    fp_new.write(i)
fp.close()
fp_new.close()
