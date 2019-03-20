#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

result = 0

for i in range(100):
    result += random.randint(0, 9)

print(result)
