#!/usr/bin/python3
"""from a repository, get the author name and commit sha using github api"""


from sys import argv
from requests import get

if __name__ == "__main__":
    try:
        repo = argv[1]
        user = argv[2]
    except IndexError:
        exit()
    except NameError:
        exit()
    url = f"https://api.github.com/repos/{user}/{repo}/commits?per_page=10"
    headers = {'Accept': 'application/vnd.github.v3+json'}
    res = get(url, headers=headers)
    if res.status_code == 200:
        data = res.json()
        for commit in data:
            commit_data = commit.get('commit')
            commiter = commit_data.get('author').get('name')
            sha = commit.get('sha')
            print("{}: {}".format(sha, commiter))
