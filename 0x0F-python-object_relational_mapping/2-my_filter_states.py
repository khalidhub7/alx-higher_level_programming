#!/usr/bin/python3

"""Lists all states + arg to find"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    conx = MySQLdb.connect(
        host='localhost', port=3306,
        user=argv[1], passwd=argv[2], database=argv[3]
    )
    curs = conx.cursor()
    query = 'SELECT * FROM states WHERE name LIKE "{}"'\
        .format(str(argv[4]))

    curs.execute(query)
    result = curs.fetchall()

    for i in result:
        print(i)

    curs.close()
    conx.close()
