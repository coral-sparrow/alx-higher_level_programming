#!/home/moi/alx/alx-venv/bin/python

##!/usr/bin/python3
import MySQLdb
# import os
import sys

uname = 'root'
password = 'root'
db = 'alx_db'
host = "192.168.1.4"
name = sys.argv[1]

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
    where binary Name like '{}' 
    order by  score desc
    '''.format(name)
    )

for i in cur.fetchall():
    print(i)
# print(type(cur.fetchall()))

# print(sys.argv)
# con = MySQLdb.Connect(

# )