#!/usr/bin/python3
'''my module'''


import sys
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file


a = []
for i in (sys.argv)[1:]:
    a.append(i)

try:
    b = load_from_json_file("add_item.json")
except Exception:
    b = []

b += a
save_to_json_file(a, "add_item.json")
