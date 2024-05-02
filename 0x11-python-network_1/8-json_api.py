#!/usr/bin/python3
""" handle status code
 using requests package"""

import requests
from sys import argv

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if argv[1]:
        data = {'q': argv[1]}
    else:
        data = {'q': ''}
    req = requests.post(url, data)

    if req.headers.get('content-type') == 'application/json':
        if req.json():
            print(f'[{req.json().get("id")}] {req.json().get('name')}')
        else:
            print('No result')
    else:
        print('Not a valid JSON')
