#!/usr/bin/python3

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as opened_url:
    responce = opened_url.read()

for i in responce:
    print(i)
