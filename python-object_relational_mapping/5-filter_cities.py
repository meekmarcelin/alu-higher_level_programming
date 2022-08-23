#!/usr/bin/python3
"""
Name the argument of the city and list it
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    check = (argv[4], )
    cur.execute("SELECT * FROM cities JOIN states\
    ON cities.state_id = states.id WHERE states.name = %s\
    ORDER BY cities.id ASC", check)
    lst = cur.fetchall()
    cities = []
    for s in lst:
        if s[4] == check[0]:
            cities.append(s[2])
    print(', '.join(cities))
    cur.close()
    db.close()
