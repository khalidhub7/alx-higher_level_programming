#!/usr/bin/python3
""" Sends a POST request """

import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email_v = argv[2]
    values = {'email': email_v}

    """ Encode the dictionary into a URL-encoded string """
    data = urllib.parse.urlencode(values)

    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    """ Convert the URL-encoded string
    to bytes using UTF-8 encoding """

    with urllib.request.urlopen(req) as page:
        """ Read the response body as bytes 
        and decode it into a UTF-8 string """
        var = page.read().decode('utf-8')

    print(var)
