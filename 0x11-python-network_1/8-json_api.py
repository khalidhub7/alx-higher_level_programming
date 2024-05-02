#!/usr/bin/python3
""" json api"""

import requests
import sys

def search_user(letter):
    url = 'http://0.0.0.0:5000/search_user'
    params = {'q': letter} if letter else {}

    response = requests.post(url, params=params)

    try:
        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if len(sys.argv) > 1:
    letter = sys.argv[1]
else:
    letter = ""

search_user(letter)
