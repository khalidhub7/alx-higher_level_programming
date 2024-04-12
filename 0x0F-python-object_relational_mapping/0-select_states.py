#!/usr/bin/python3

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    _data = MySQLdb.connect(host='localhost', port=3306,
    user=argv[1], passwd=argv[2], database=argv[3])

    _cursor = _data.cursor()
    _query = "SELECT * FROM states"

    _cursor.execute(_query)
    result = _cursor.fetchall()

    for i in result:
        print(i)

    _cursor.close()
    _data.close()
