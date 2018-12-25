#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 神奇8球
import random

messages = ['It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']         # 列表中 可以不考虑缩进

print(messages[random.randint(0, len(messages) - 1)])