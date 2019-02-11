#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 计算存款利息
# 4中方法可选：
# 活期，年利率为r1；
# 一年期定期，年利率为r2；
# 存两次半年期定期，年利率为r3；
# 两年期定期，年利率为r4
# 现有本金1000元，请分别计算出一年后按4种方法所得到的本息和
# 提示：本息 = 本金 + 本金* 年利率*存款期

principal = 1000
term = 1
r1 = 0.1
r2 = 0.2
r3 = 0.3
r4 = 0.4

pri1 = principal + principal * r1 * term
pri2 = principal + principal * r2 * term
pri3 = (principal + principal * r3 * term/2) + (principal + principal * r3 * term/2) * r3 * term/2
pri4 = principal + principal * r4 * term

print("第一种本息和为：", pri1)
print("第二种本息和为：", pri2)
print("第三种本息和为：", pri3)
print("第四种本息和为：", pri4)