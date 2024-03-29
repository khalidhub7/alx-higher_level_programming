#!/usr/bin/python3
'''
get and print all states
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    datab = MySQLdb.connect(user=argv[1], passwd=argv[2], database=argv[3])
    curr = datab.cursor()
    myquery = "SELECT id, name FROM states ORDER BY id ASC;"
    curr.execute(myquery)
    results = curr.fetchall()
    for i in results:
        print(i)
    curr.close()
    datab.close()
