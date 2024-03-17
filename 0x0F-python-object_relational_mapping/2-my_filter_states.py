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
    myquery = "SELECT * FROM states ORDER BY id {};".format("ASC")
    curr.execute(myquery)
    results = curr.fetchall()
    for i in results:
        if i[1] == argv[4]:
            print(i)
    curr.close()
    datab.close()
