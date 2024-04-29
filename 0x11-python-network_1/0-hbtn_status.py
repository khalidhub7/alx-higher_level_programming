#!/usr/bin/python3
'''Fetches a URL'''

import urllib.request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        page = response.read()
    print('Body response:\n'
          f'\t- type: {type(page)}\n'
          f'\t- content: {page}\n'
          f'\t- utf8 content: {page.decode("utf8")}')
