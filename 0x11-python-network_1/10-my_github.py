#!/usr/bin/python3
"""last mnd task"""

from sys import argv
from requests import get

if __name__ == "__main__":
    username = argv[1]
    url = "https://api.github.com/users/{}".format(username)
    password = argv[2]
    password_dict = {'Authorization': f"token {password}"}
    res = get(url, headers=password_dict)

    if res.status_code == 200:
        data = res.json()
        user_id = data.get("id")
        print(user_id)
    else:
        print("None")
