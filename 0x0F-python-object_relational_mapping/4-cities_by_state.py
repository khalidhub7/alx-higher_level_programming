#!/usr/bin/python3
"""  lists all cities from the database  """

import MySQLdb
from sys import argv
if __name__=='__main__':
    datab = MySQLdb.connect(
        user=argv[1], passwd=argv[2], database=argv[3]
    )
    curs = datab.cursor()
    query =  "SELECT * FROM cities ORDER BY id ASC"
    curs.execute(query)
    results = curs.fetchall()
    for i in results:
        print(i)
