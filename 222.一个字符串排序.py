# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 一个字符串排序，排序规则：小写<大写<奇数<偶数

# 原理：先比较元组的第一个值，FALSE<TRUE，如果相等就比较元组的下一个值，以此类推

# 小写<大写<奇数<偶数
# 偶数(True,True,False,False)
# 奇数(True,False,False,False)
# 大写(False,False,True,False)
# 小写(False,False,False,True)

s = '9a13C85c7B24A6b'
# 正确的顺序应该为：abcABC135792468
lis = sorted(s, key=lambda x:(x.isdigit(), x.isdigit() and int(x) % 2 == 0, \
    x.isalpha() and x.isupper(), x.isalpha() and x.lower()))

print(''.join(lis))
