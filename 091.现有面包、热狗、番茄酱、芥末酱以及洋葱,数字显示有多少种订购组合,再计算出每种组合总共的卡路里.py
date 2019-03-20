#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 现有面包、热狗、番茄酱、芥末酱以及洋葱，数字显示有多少种订购组合
# 其中面包必订，0不订，1订，比如10000，表示只订购面包，给出每种食物的卡路里（自定义）
# 再计算出每种组合总共的卡路里

bread_cal = 40
hotdog_cal = 50
ketchup_cal = 60
wasabi_cal = 45
onion_cal = 30

count = 0
for bread in[1]:
    for hotdog in[0,1]:
        for ketchup in[0,1]:
            for wasabi in[0,1]:
                for onion in[0,1]:
                    total_cal = (bread_cal*bread + hotdog_cal*hotdog + ketchup_cal*ketchup + wasabi_cal*wasabi + onion_cal*onion)
                    print(bread,hotdog,ketchup,wasabi,onion,total_cal,"cal")
                    count += 1
print("There are ",count," kinds of type!")