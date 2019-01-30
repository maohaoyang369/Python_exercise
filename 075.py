#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 列表重排

a =[2, 2, 3, 3, 4, 4, 5, 6]
result = []        # 生成一个空列表，存储排重后的元素
for i in a:        # 遍历列表的每个元素
   if i not in result:        # 判断是否在列表中，如果不在，就添加到列表中
        result.append(i)
print(result)