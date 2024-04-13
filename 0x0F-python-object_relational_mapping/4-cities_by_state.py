#!/usr/bin/python3

""" lists all cities """

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    conx = MySQLdb.connect(
        host='localhost', port=3306, 
        user=argv[1], passwd=argv[2], database=argv[3]
    )
    curs = conx.cursor()
    query = "SELECT cities.id, cities.name, states.name \
        FROM cities \
            INNER JOIN states ON cities.state_id = states.id;"

    curs.execute(query)
    result = curs.fetchall()
    for i in result:
        print(i)
