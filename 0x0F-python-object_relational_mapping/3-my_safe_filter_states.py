#!/usr/bin/python3
''' same as last code, but safe from MySQL injections! '''
import MySQLdb
from sys import argv
if __name__ == '__main__':
    datab = MySQLdb.connect(user=argv[1], passwd=argv[2],
    database=argv[3], state_searched=argv[4])
    curr = datab.cursor()
    myquery = 'SELECT id, name FROM states\
    WHERE name = %s ORDER BY id {};'.format('ASC')
    curr.execute(myquery, (argv[4],))
    results = curr.fetchall()
    for i in results:
        print(i)
