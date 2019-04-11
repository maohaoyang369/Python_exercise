# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 通过文件处理数据

# 数据文件：data.log
# 20160215 000148|0|collect info job start|success|
# 20160215000153|0|collect info job
# end|success|resultcode = 0000
# 20160216000120|0|collect info job start|success|
# 20160216000121|0|collect info job
# end|success|resultcode = 0000
# 20160217000139|0|collect info job start|success|
# 20160217000143|0|collect info job
# end|success|resultcode = 0000

# 数据分析需求：
# 每行内容需要生成以每行首年月日为名称的文件，文件内容写入|0|后的所有行内容（也包括|0| ）

with open("d:\\python\\a.txt") as fp:
    for line in fp:
        file_name = line.split("|", 1)[0]
        file_content = line.split("|", 1)[1]
        with open("d:\\python\\" + file_name + ".txt", "w") as fp1:
            fp1.write("|" + file_content + "\n")
