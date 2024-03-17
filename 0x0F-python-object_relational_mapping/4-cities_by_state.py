#!/usr/bin/python3
"""Lists all cities from the database"""

import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python script.py username password database_name")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        datab = MySQLdb.connect(user=username, passwd=password, database=database_name)
        curs = datab.cursor()
        query = "SELECT * FROM cities ORDER BY id ASC"
        curs.execute(query)
        results = curs.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if curs:
            curs.close()
        if datab:
            datab.close()
