#!/usr/bin/python3
""" lists all State """
import MySQLdb
import sys
from model_state import Base, State

if __name__ == "__main__":
    datab = MySQLdb.connect(host="localhost", user=sys.argv[1],
    passwd=sys.argv[2], database=sys.argv[3])
    curs = datab.cursor()
    query = "SELECT * FROM states"
    curs.execute(query)
    results = curs.fetchall()
    for i in results:
        print("{}: {}".format(i[0], i[1]))
