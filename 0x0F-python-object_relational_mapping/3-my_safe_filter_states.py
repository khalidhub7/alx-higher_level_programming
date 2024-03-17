#!/usr/bin/python3
''' same as last code, but safe from MySQL injections! '''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Check if all required arguments are provided
    if len(argv) < 5:
        print("Usage: python script.py <username> <password> <database> <state_searched>")
        exit(1)
    
    # Establish a connection to the database
    datab = MySQLdb.connect(user=argv[1], passwd=argv[2], database=argv[3])
    curr = datab.cursor()

    # Use placeholders to avoid SQL injection
    myquery = 'SELECT id, name FROM states WHERE name = %s ORDER BY id ASC;'
    curr.execute(myquery, (argv[4],))
    
    # Fetch and print results
    results = curr.fetchall()
    for row in results:
        print(row)

    # Close the cursor and database connection
    curr.close()
    datab.close()
