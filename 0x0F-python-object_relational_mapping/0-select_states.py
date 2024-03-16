#!/usr/bin/python3

import MySQLdb

db = MySQLdb.connect(username='', passwd='', database='')
curr = MySQLdb.cursor()
query = "SELECT * FROM hbtn_0e_0_usa"
curr.execute(query)
resu = curr.fettchall()
for i in resu:
    print(i)
db.close()
curr.close()
