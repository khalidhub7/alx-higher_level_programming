#!/usr/bin/python3
"""Get and print states table with a filter passed as an argument."""

import MySQLdb
from sys import argv

def process():
    datab = MySQLdb.connect(
        user=argv[1], passwd=argv[2], database=argv[3]
    )
    curs = datab.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    curs.execute(query)
    results = curs.fetchall()
    for i in results:
        if i[1] == argv[4]:
            print(i)

if __name__ == '__main__':
    process()
