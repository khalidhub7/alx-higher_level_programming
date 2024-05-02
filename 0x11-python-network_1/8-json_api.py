#!/usr/bin/python3
""" json api"""

import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) < 2:
        print('Usage: ./script_name.py <search_query>')
    else:
        url = 'http://0.0.0.0:5000/search_user'
        data = {'q': argv[1]}
        req = requests.post(url, data=data)

        if req.headers.get('content-type') == 'application/json':
            try:
                response_json = req.json()
                if 'id' in response_json and 'name' in response_json:
                    print(f'[{response_json["id"]}] {response_json["name"]}')
                else:
                    print('No result')
            except ValueError:
                print('Invalid JSON format')
        else:
            print('Not a valid JSON')
