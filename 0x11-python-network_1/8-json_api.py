#!/usr/bin/python3
"""post a letter, get id and name(name that match that letter)"""


from sys import argv
from requests import post

if __name__ == "__main__":
    try:
        q = argv[1]
    except IndexError:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}
    req = post(url, data=data)

    if req.headers.get('content-type') == 'application/json':
        content = req.json()
        if content:
            the_id = content.get('id')
            name = content.get('name')
            print("[{}] {}".format(the_id, name))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
