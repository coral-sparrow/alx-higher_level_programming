#!/home/moi/alx/alx-venv/bin/python

##!/usr/bin/python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

uname = 'root'
password = 'root'
db = 'alx_db'
host = "192.168.1.4"



def connectToDB():
    '''connect to db code'''
    engine = create_engine('mysql+pymysql://root:root@192.168.1.4/alx_db', echo=True)
    Base = declarative_base()

    class State(Base):
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True, nullable=False)
        name =  Column(String(50))

    Base.metadata.create_all(engine)

connectToDB()