#!/usr/bin/python3

""" lists all states with some filter """

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    conx = MySQLdb.connect(
        host='localhost', port=3306, 
        user=argv[1], passwd=argv[2], db=argv[3]
        )
    query = 'SELECT * FROM states'
    _curs = conx.cursor()

    _curs.execute(query)
    result = _curs.fetchall()

    for i in result:
        if str(i[1]).startswith('N'):
            print(i)
    
    _cursor.close()
    conx.close()
