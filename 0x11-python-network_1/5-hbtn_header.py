#!/usr/bin/python3
""" get header using requests """

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    header_key = 'X-Request-Id'
    req = requests.get(url)
    value = req.headers[header_key]
    print(value)
