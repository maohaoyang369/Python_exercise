# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入高考的5个成绩，700以上，打印可以上清华大学了，600--700打印，可以上重点大学了，
# 500--600可以上一本了，400-500,打印可以上大专了，400以下打印请重头再来

total = 0
for i in range(5):
    result = input("Please enter your result：")
    for j in result:
        if j not in "01234567890.":
            print("None")
    total += float(result)
print("总成绩：", total)

if total > 700:
    print("可以上清华大学了")
elif 600 <= total <= 700:
    print("可以上重点大学了")
elif 500 <= total <= 600:
    print("可以上一本了")
elif 400 <= total <= 500:
    print("可以上大专了")
elif total < 400:
    print("请重头再来")
