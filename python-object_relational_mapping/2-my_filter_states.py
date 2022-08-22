#!/usr/bin/python3
""" Display all values in states """
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'\ ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()
    for s in rows:
        if s[1] == argv[4]:
            print(s)
    cur.close()
    db.close()

