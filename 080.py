#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 3个人在餐厅吃饭，想分摊饭费。总共花费35.27美元，他们还想给15%的小费。每个人该怎么付钱

prices = 35.27 * (15/100) + 35.27
oneperson_pay = prices/3
print(oneperson_pay)