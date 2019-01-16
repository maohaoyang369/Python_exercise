#!/usr/bin/env python
# # -*- coding: utf-8 -*-

# 检测密码强度
# c1 : 长度>=8
# c2: 包含数字和字母
# c3: 其他可见的特殊字符
# 强：满足c1,c2,c3
# 中: 只满足任一2个条件
# 弱：只满足任一1个或0个条件

import string


def pin_intensity(pin):
    c1 = False
    c2 = False
    c3 = False
    c4 = False
    c5 = False
    if len(pin) >= 8:
        c1 = True
    for i in pin:
        if i in string.ascii_letters:
            c4 = True
        elif i in string.digits:
            c5 = True
        elif i in string.punctuation:
            c3 = True
        if c4 and c5:
            c2 = True
    result = [c1, c2, c3]
    if result.count(True) == 3:
        return "The pin is strong!"
    elif result.count(True) == 2:
        return "The pin is middle!"
    else:
        return "The pin is weak"


print(pin_intensity("rytuy657878@#"))
print(pin_intensity("444rr4"))
print(pin_intensity("rytuy657878"))
print(pin_intensity("4444"))



