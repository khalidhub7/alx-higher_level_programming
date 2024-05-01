#!/usr/bin/python3
""" fetch using package requests """

import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    req = requests.get(url)
    print(f'Body response:\n\t- type: {type(req.text)}')
    print(f'\t- content: {req.text}')
