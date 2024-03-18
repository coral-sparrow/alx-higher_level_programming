#!/usr/bin/python3
'''this is mysql db with python operations'''


import MySQLdb
import sys


def connectToDB() -> None:
    '''connect to db func'''
    uname = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    host = "localhost"

    con = MySQLdb.connect(
        user=uname,
        password=password,
        database=db,
        host=host
        )

    cur = con.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")

    for i in cur.fetchall():
        print(i)

    cur.close()
    con.close()


if __name__ == "__main__":
    connectToDB()
