#!/usr/bin/python3

import urllib

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.URLopener(url) as opened_url:
    responce = opened_url.read()
for i in reading:
    print(i)
