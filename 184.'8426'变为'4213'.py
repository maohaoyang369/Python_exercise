# !/usr/bin/env python
# -*- coding: utf-8 -*-

# "8426"变为"4213"

example = "8426"
result = ""

for i in example:
    result = str(int(int(example)/2))

print(result)
