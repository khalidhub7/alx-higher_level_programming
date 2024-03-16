#!/usr/bin/python3
'''
get and print all states'''


if __name__=='__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
    database=argv[3])
    curr = db.cursor()
    myquery = "SELECT id, name FROM states ORDER BY id ASC;"
    curr.execute(myquery)
    results = cur.fetchall()
    for i in results:
        print(i)
    curr.close()
    db.close()
