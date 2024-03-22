#!/home/moi/alx/alx-venv/bin/python

##!/usr/bin/python3

from sqlalchemy import Column, Integer, String, create_engine
# from sqlalchemy.orm import declarative_base
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

uname = 'root'
password = 'root'
db = 'alx_db'
host = "192.168.1.4"



def connectToDB():
    '''connect to db code'''
    engine = create_engine(f'mysql+pymysql://{uname}:{password}@{host}/{db}', echo = True)
    Session = sessionmaker(bind=engine)

    session = Session()
    for instance in session.query(State).order_by(State.id):
        print (f'{instance.id}: {instance.name}')
    # Base = declarative_base()

    # class State(Base):
    #     __tablename__ = 'states'
    #     id = Column(Integer, primary_key=True, nullable=False)
    #     name =  Column(String(50))

    # Base.metadata.create_all(engine)

connectToDB()