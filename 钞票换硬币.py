#!/usr/bin/env python
# -*- coding: utf-8 -*-


residue = 100
count = 0
result = []

for i in range(int(residue/1)):
    for m in range(int(residue/2)):
        for n in range(int(residue/5)):
            if (i + m * 2 + n * 5) == 100 and i != 0 and m != 0 and n != 0:
                count += 1
                result.append((i, m, n))
print(count)
print(result)