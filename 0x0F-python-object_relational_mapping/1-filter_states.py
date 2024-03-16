#!/usr/bin/python3
'''
get and print all states
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    datab = MySQLdb.connect(user=argv[1], passwd=argv[2], database=argv[3])
    curr = datab.cursor()
    start_with = "N"
    myquery = "SELECT id, name FROM states WHERE name\
         LIKE '{}%' ORDER BY id ASC;".format(start_with)
    curr.execute(myquery)
    results = curr.fetchall()
    for i in results:
        print(i)
    curr.close()
    datab.close()
