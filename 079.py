#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 计算一周有多少分钟、多少秒钟

sec = 1
one_minute = 60 * sec
one_hour = 60 * one_minute
one_day = 24 * one_hour
one_week = 7 * one_day
total_week_secs = int(one_week)
total_week_minutes = int(total_week_secs/one_minute)
print(total_week_secs)
print(total_week_minutes)