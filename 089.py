#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 长途旅行中，刚到一个加油站，距下一个加油站还有200km，而且以后每个加油站之间距离都是200km。
# 编写一个程序确定是不是需要在这里加油，还是可以等到接下来的第几个加油站再加油。
# 程序询问一下几个问题：
# 1.你车的油箱多大，单位升
# 2.目前油箱还剩多少油，按百分比算，比如一半就是0.5
# 3.你车每升油可以走多远（km）
# 提示：油箱中包含5升的缓冲油，以防油表不准

volume = input("How large is your tank：")
oil_remain_percent= input("How much oil is left in your car：")
distance = input("How far is the oil per liter of your car：")   

waste_oil = 200/float(distance)        # 200km 消耗多少油
oil_remain = float(volume) * float(oil_remain_percent)        # 油箱剩余油量

if oil_remain - waste_oil < 0:
    print("Please refuel your car")
else:
    print("You can refuel at the next gas station")