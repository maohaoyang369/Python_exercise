#!/usr/bin/env python
# -*- coding: utf-8 -*-

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

url_link = "http://www.sohu.com"

new_url = list()


def fitler_url(url_l):
    response = requests.get(url_l)
    h_content = re.findall(r"[a-zA-z]+://[^\s]*", response.text)
    for sigal_url in h_content:
        if re.match(r".*\.(jpg|css|js|png|jpeg)$", sigal_url):
            pass
        elif re.match(r".*\>", sigal_url):
            pass
        else:
            new_url.append(sigal_url)


fitler_url(url_link)

print(new_url)

