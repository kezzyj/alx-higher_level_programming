#!/usr/bin/python3

"""

python script that lists all cities from the database hbtn_0e_4_usa

with specified state name

"""



import MySQLdb

from sys import argv



if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],

                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (argv[4],))

    rows = cursor.fetchall()

    print(", ".join(city[0] for city in rows))

    cursor.close()

