#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 现有面包、热狗、番茄酱、芥末酱以及洋葱，数字显示有多少种订购组合
# 其中面包必订，0不订，1订，比如10000，表示只订购面包

import pprint

count = 0
for bread in[1]:
    for hotdog in[0,1]:
        for ketchup in[0,1]:
            for wasabi in[0,1]:
                for onion in[0,1]:
                    print(bread,hotdog,ketchup,wasabi,onion)
                    count += 1
print("There are ",count," kinds of type!")