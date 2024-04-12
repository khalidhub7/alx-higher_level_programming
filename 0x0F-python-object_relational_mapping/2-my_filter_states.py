#!/usr/bin/python3

"""Lists all states + arg to find"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    _data = MySQLdb.connect(
        host='localhost', port=3306,
        user=argv[1], passwd=argv[2], database=argv[3]
    )
    _curs = _data.cursor()
    _query = 'SELECT * FROM states WHERE name LIKE "{}"'.format(argv[4])

    _curs.execute(_query)
    result = _curs.fetchall()

    for i in result:
        print(i)
    
    _curs.close()
    _data.close()
