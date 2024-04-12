#!/usr/bin/python3

""" lists all states using py """

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    conx = MySQLdb.connect(
        host='localhost', port=3306, 
        user=argv[1], passwd=argv[2], database=argv[3]
        )

    _cursor = conx.cursor()
    query = "SELECT * FROM states"

    _cursor.execute(query)
    result = _cursor.fetchall()

    for i in result:
        print(i)

    _cursor.close()
    _data.close()
