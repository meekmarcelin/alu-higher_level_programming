#!/usr/bin/python3
"""Change the name of State in db
"""
import sys
from sqlalchemy.orm import session
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = session(engine)
    session = Session()

    res = session.query(State).filter(State.id == 2)
    res.update({"name": ("New Mexico")})

    session.commit()
