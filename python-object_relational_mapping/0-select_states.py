#!/usr/bin/python3
""" List all the states """
import MySQLdb
import sys


def get_states():
    """ list the arguments

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """
    db = MySQLdb.connect(user=argv[1], passwd=.argv[2], db.argv[3])

    cur = db.cursor()

    cur.execute("select * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for i in rows:
        print(i)

    cur.close()
    db.close()

    if __name__ == "__main__":
        get_states()
