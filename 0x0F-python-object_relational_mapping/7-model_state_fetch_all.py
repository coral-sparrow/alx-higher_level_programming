#!/usr/bin/python3
'''this is mysql db with python operations'''


from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def connectToDB():
    '''connect to db func'''

    uname = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    host = "localhost"

    engine = create_engine(f'mysql+pymysql://{uname}:{password}@{host}/{db}')

    Session = sessionmaker(bind=engine)

    session = Session()
    for instance in session.query(State).order_by(State.id):
        print(f'{instance.id}: {instance.name}')


if __name__ == "__main__":
    connectToDB()
