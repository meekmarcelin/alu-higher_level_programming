#!/usr/bin/python3
"""Add the State Louisiana
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

    state = State(name='Louisiana')
    session.add(state)
    session.commit()

    print(state.id)
