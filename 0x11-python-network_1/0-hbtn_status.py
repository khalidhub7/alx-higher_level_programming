#!/usr/bin/python3
""" that fetches """


import urllib.request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as responce:
        page = responce.read()
    print('Body response:\n\
    - type: {}\n\
    - content: {}\n\
    - utf8 content: {}'\
    .format(type(page), page, page.decode('utf8')))
