# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 按照key的大小顺序升序进行输出，输出key=value，d={-1:100,-2:200,0:300,-3:200}
# -3=200,-2=200,-1=100,0=300

d = {-1:100, -2:200, 0:300, -3:200}

for key in sorted(d.keys()):
    print("%s = %s ," % (key, d[key]), end=" ")
