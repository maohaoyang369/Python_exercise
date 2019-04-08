# !/usr/bin/env python
# -*- coding: utf-8 -*-

# max()排序 [1,-1,2,-2,3,-3] 每次找到列表最大值，存到新的list，
# 在老的list里面删掉一个。继续重复上面的过程，直到所有的元素都到新list.
# 1 升序
# 2 降序

# 第一种方法：

a = [1, -1, 2, -2, 3, -3]

result = []

for i in range(len(a)):
    result.append(max(a))
    a.remove(max(a))

print(result)
result.reverse()
print(result)

# 第二种方法：

a = [1, -1, 2, -2, 3, -3]

result = []

for i in range(len(a)):
    result.insert(0, max(a))
    a.remove(max(a))

print(result)
