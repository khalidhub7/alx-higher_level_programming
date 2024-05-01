#!/usr/bin/python3
""" Sends a POST request """

import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    data = {
        'email': argv[2]
    }
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as post:
        page = post.read().decode("utf-8")
    print(page)
