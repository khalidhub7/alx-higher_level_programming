#!/usr/bin/python3

import MySQLdb

if __name__=='__main__':
    db = MySQLdb.connect(host="localhost", user='', passwd='', database='')
    curr = MySQLdb.cursor()
    query = "SELECT * FROM hbtn_0e_0_usa"
    curr.execute(query)
    resu = curr.fettchall()
    for i in resu:
        print(i)
    db.close()
    curr.close()
