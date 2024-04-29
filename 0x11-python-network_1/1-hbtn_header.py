#!/usr/bin/python3
'''displays value of variable
 in header'''


import urllib.request
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        value = response.getheader("X-Request-Id")
    print(value)
