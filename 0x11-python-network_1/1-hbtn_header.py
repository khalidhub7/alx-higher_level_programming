#!/usr/bin/python3
'''displays value of variable
 in header'''


import urllib.request
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    header_key = 'X-Request-Id'
    with urllib.request.urlopen(url) as res:
        value = res.headers[header_key]
    print(value)
