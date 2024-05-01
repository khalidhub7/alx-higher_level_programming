#!/usr/bin/python3
""" post using requests package"""

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    req = requests.get(url)
    if req.code_status >= 400:
        print(f'Error code: {req.code_status}')
    else:
        print(req.text)
