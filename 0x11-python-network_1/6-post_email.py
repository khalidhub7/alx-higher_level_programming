#!/usr/bin/python3
""" post using requests package"""

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = argv[2]
    data = {
        'email': email
    }
    req = requests.post(url, data)
    print(req.json().decode())
