#!/usr/bin/python3
""" get and print all states with simple filter """

import MySQLdb
from sys import argv

if __name__ == '__main__':

    datab = MySQLdb.connect(
        user=argv[1], passwd=argv[2], database=argv[3]
    )
    curr = datab.cursor()
    myquery = "SELECT id, name FROM states WHERE name\
         LIKE 'N%' ORDER BY id ASC;"
    curr.execute(myquery)
    results = curr.fetchall()
    for i in results:
        if i[1][0] == "N":
            print(i)
    curr.close()
    datab.close()
