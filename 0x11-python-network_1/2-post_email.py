#!/usr/bin/python3
""" Sends a POST request """

import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email_v = argv[2]
    values = {'email': email_v}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as page:
        var = page.read().decode('utf-8')

    print(var)
