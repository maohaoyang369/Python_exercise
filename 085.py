#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 一家商场在降价促销，如果购买金额50-100元（包含50元和100元）之间，会给10%的折扣，如果购买金额大于100元会给20%折扣。
# 写一程序，询问购买价格，再显示出折扣（10%或20%）和最终价格

price = input("How much are they? They are: ")
if 50 <= float(price) <= 100:
    price = float(price) * ((100-10)/100)
    print(price)
elif  float(price) > 100:
    price = float(price) * ((100-20)/100)
    print(price)
else:
    print(price)