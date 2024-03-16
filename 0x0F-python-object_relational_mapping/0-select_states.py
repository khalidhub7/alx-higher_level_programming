#!/usr/bin/python3

import MySQLdb

if __name__=='__main__':
    db = MySQLdb.connect(user='', passwd='', database='')
    curr = MySQLdb.cursor()
    query = "SELECT * FROM hbtn_0e_0_usa"
    curr.execute(query)
    resu = curr.fetchall()
    for i in resu:
        i[0] = state.id
    db.close()
    curr.close()
