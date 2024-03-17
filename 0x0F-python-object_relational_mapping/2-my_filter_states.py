#!/usr/bin/python3
""" get and print states 
with some filter passing by arg"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    datab = MySQLdb.connect(
        user=argv[1], passwd=argv[2], database=argv[3]
    )
    curr = datab.cursor()
    look = argv[4]
    myquery = "SELECT id, name FROM states WHERE name\
         LIKE 'N%' ORDER BY id ASC;"
    curr.execute(myquery)
    results = curr.fetchall()
    for i in results:
        if i[1][0] == look:
            print(i)
    curr.close()
    datab.close()
