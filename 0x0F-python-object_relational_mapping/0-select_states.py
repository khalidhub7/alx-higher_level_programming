#!/usr/bin/python3
'''
get and print all states
'''

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], database=sys.argv[3])
    curr = db.cursor()
    myquery = "SELECT id, name FROM states ORDER BY id ASC;"
    curr.execute(myquery)
    results = curr.fetchall()
    for i in results:
        print(i)
    curr.close()
    db.close()
