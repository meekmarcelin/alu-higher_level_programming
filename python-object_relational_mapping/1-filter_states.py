#!/usr/bin/python3
""" list all states with name starting upper N """


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    states = cr.fetchall()
    for state in states:
        if state[1][0] == 'N':
            print(state)
    cr.close()
    db.close()
