#!/usr/bin/python3
'''Fetches a URL'''

import urllib.request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as reponce:
        page = reponce.read()
    print('Body response:\n\t- type: {}\n\t\
- content: {}\n\t- utf8 content: {}\n'\
.format(type(page), page, page.decode('utf-8')))
