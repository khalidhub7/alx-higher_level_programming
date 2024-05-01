#!/usr/bin/python3
""" post using requests package"""

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print(f'Error code: {req.status_code}')
    else:
        print(req.text)
