#!/usr/bin/python3
'''this is mysql db with python operations'''

import MySQLdb
import sys

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
cur.execute(
    '''
    select * from states
    order by  id desc
    '''
    )

for i in cur.fetchall():
    print(i)
