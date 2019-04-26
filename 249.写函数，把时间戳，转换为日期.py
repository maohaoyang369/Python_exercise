# !/usr/bin/env python
# -*- encoding: utf-8 -*-

# 把一个多级目录中所有文件的字母删除


import time
import datetime
import locale
locale.setlocale(locale.LC_CTYPE, 'chinese')     # 设定当时


def current_date():
    current = time.localtime()
    year = str(current[0])
    mon = str(current[1])
    day = str(current[2])
    return year+'年'+mon+"月"+day+'日'


def current_time():
    current = time.localtime()
    hour = str(current[3])
    minute = str(current[4])
    second = str(current[5])
    return hour+'小时'+minute+"分钟"+second+'秒'


def current():
    current = time.localtime()
    year = str(current[0])
    mon = str(current[1])
    day = str(current[2])
    hour = str(current[3])
    minute = str(current[4])
    second = str(current[5])
    return year+'年'+mon+"月"+day+'日'+hour+'小时'+minute+"分钟"+second+'秒'


def fromTimestampToDate(timestemp):
    date_tuple = time.localtime(timestemp)
    return time.strftime("%Y年%m月%d日", date_tuple)


def fromTimestampToDateAndTime(timestemp):
    date_tuple = time.localtime(timestemp)
    return time.strftime("%Y年%m月%d日 %H小时%M分钟%S秒", date_tuple)


if __name__ == "__main__":
    print(current_date())
    print(current_time())
    print(current())
    print(fromTimestampToDate(1540711260.8172925))
    print(fromTimestampToDateAndTime(1540711260.8172925))
