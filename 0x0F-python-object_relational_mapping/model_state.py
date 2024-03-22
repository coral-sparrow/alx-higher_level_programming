#!/usr/bin/python3
'''this is mysql db with python operations'''


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


# def connectToDB():
#     '''connect to db code'''
# engine = create_engine('mysql+pymysql://root:root@localhost/hbtn_0e_6_usa')
Base = declarative_base()


class State(Base):
    '''State mapper to states table'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128))

# Base.metadata.create_all(engine)


# if __name__ == "__main__":
    # connectToDB()
