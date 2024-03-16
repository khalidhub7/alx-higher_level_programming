#!/usr/bin/python3


import MySQLdb
import sys

def list_states(username, password, database):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(user=username, passwd=password, db=database)
        curr = db.cursor()

        # Execute SQL query to fetch states sorted by states.id
        query = "SELECT * FROM states ORDER BY states.id ASC"
        curr.execute(query)
        states = curr.fetchall()

        # Display results
        print("States:")
        for state in states:
            print(f"{state[0]}: {state[1]}")

        # Close cursor and database connection
        curr.close()
        db.close()
