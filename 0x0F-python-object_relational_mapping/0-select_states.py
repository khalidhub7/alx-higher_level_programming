#!/usr/bin/python3

"""Lists all states using PyMySQL."""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    conx = MySQLdb.connect(
        host='localhost', port=3306,
        user=argv[1], passwd=argv[2], database=argv[3]
    )

    cursor = conx.cursor()
    query = "SELECT * FROM states"

    cursor.execute(query)
    result = cursor.fetchall()

    for i in result:
        print(i)

    cursor.close()
    conx.close()
