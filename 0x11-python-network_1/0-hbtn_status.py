#!/usr/bin/python3
"""script that fetches an url"""


from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        html = response.read()

    print("Body response:")
    print("{}- type: {}".format("\t", type(html)))
    print("{}- content: {}".format("\t", html))
    print("{}- utf8 content: {}".format("\t", html.decode("utf-8")))
