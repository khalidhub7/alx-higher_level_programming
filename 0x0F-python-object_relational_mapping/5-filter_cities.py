#!/usr/bin/python3

"""Lists all cities with some filter."""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    conx = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2], db=argv[3]
    )

    curs = conx.cursor()
    query = 'SELECT cities.id, cities.name, states.name ' \
            'FROM cities INNER JOIN states ' \
            'ON states.id = cities.state_id'

    curs.execute(query)
    results = curs.fetchall()
    mylist = [city[1] for city in results if city[2] == argv[4]]
    print(", ".join(mylist))
