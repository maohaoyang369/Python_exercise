# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 声明一个实例来实现：初始化一个车里有多少升油，调用run方法，实现车的运行，没油的时候提示，需要加油了。
# 跑一次，里程数加100公里，调用add_gas方法可以实现加油，让车继续运行。
# check_distance方法查看车跑的里程数

# 第一种方法


class Car(object):
    def __init__(self, fuel, distance):
        self.fuel_volume = 100
        self.fuel = fuel
        self.distance = distance

    def run(self):
        if self.fuel <= 20:
            print("The fuel volume is empty")
            return None
        self.fuel -= 20
        self.distance += 100
        return "Good"

    def add_fuel(self, n):
        if n + fuel_volume > 100:
            print("It's enough")
            return None
        fuel_volume += n
        return fuel_volume

    def check_distance(self):
        return self.distance


c = Car(30, 100)
print(c.run())    # 每次运行都会把相应的数据存在内存中，所以每次print 是在上一次print数据的基础之上，不像函数，不保存数据
print(c.run())
print(c.check_distance())

# 第二种方法


class CAR(object):
    CAR_NUM = 0

    def __init__(self, name, length, height, color, gas_num, gas_consume_num, distance):
        self.name = name
        self.length = length
        self.height = height
        self.color = color
        self.gas_num = gas_num
        self.gas_consume_num = gas_consume_num
        self.distance = distance

    def run(self):
        if self.gas_num >= self.gas_consume_num:
            self.distance += 100 
            self.gas_num -= 20 
        else:
            print("没油了，请速加！")

    def add_gas(self, n):
        self.gas_num += n

    def check_distance(self):
        return self.distance

    def check_gas(self):
        return self.gas_num

c = CAR("豪车", "500cm", "200cm", "red", 100, 20, 0)

for i in range(5):
    c.run()
    print(c.check_gas())

print(c.check_distance())
c.add_gas(100)
print(c.check_gas())
