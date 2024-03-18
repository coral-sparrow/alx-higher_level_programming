#!/home/moi/alx/alx-venv/bin/python

##!/usr/bin/python3
import MySQLdb
# import os
import sys

uname = sys.argv[1]
password = sys.argv[2]
db = sys.argv[3]
host = "192.168.1.4"

con = MySQLdb.connect(
    user = uname,
    password = password,
    database = db,
    host = host
    )

cur = con.cursor()
cur.execute(
    '''
    select * from second_table
    order by  score desc
    '''
    )

for i in cur.fetchall():
    print(i)
# print(type(cur.fetchall()))

# print(sys.argv)
# con = MySQLdb.Connect(

# )