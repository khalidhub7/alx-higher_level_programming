#!/usr/bin/python3
'''my module'''


import json
import sys
from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file


a = []
for i in (sys.argv)[1:]:
    a.append(i)
save_to_json_file(a, "add_item.json")
load_from_json_file("add_item.json")
