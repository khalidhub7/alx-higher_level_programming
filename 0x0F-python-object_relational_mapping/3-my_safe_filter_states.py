#!/usr/bin/python3
''' same as last code, but safe from MySQL injections! '''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    datab = MySQLdb.connect(
        user=argv[1], passwd=argv[2],
        database=argv[3]
    )
    curr = datab.cursor()
    """ Use placeholders to avoid SQL injection """
    myquery = 'SELECT id, name FROM states WHERE name = %s ORDER BY id ASC;'
    curr.execute(myquery, (argv[4],))
    results = curr.fetchall()
    for row in results:
        print(row)
    curr.close()
    datab.close()
