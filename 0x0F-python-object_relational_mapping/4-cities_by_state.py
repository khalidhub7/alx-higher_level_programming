#!/usr/bin/python3
""" all cities from the database """

import MySQLdb
from sys import argv

if __name__=='__main__':
    datab = MySQLdb.connect(
        user=argv[1], passwd=argv[2], database=argv[3]
    )
    curs = datab.cursor()

    query = "SELECT cities.id, cities.name, states.name \
    FROM cities \
    JOIN states ON cities.state_id = states.id \
    ORDER BY cities.id ASC"

    curs.execute(query)
    results = curs.fetchall()
    for i in results:
        print(i)
