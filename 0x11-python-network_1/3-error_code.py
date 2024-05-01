#!/usr/bin/python3
""" handle error """

import urllib.request
from sys import argv
from urllib.error import HTTPError

if __name__ == '__main__':
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as page:
            page = page.read().decode('utf-8')
        print(page)
    except HTTPError as rr:
        print(f'Error code: {rr.code}')
