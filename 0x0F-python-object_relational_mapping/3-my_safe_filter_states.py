#!/usr/bin/python3

""" Lists all states matching a given pattern
    and handles SQL injection """

import MySQLdb
import sys

if __name__ == '__main__':
    conx = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], database=sys.argv[3]
    )

    curs = conx.cursor()
    query = 'SELECT * FROM states WHERE name LIKE %s'
    # Prevent SQL injection by passing arguments in execute()
    curs.execute(query, (sys.argv[4],))

    result = curs.fetchall()
    for i in result:
        print(i)

    curs.close()
    conx.close()
