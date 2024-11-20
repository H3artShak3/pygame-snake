from datetime import date

from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.util import deprecations

deprecations.SILENCE_UBER_WARNING = True

engine = create_engine("sqlite:///game.db")
Base = declarative_base()


class GameBase(Base):
    __tablename__ = "top_score"
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    score = Column(Integer)
    data = Column(Date)

    def __init__(self, user_name, score):
        self.user_name = user_name
        self.score = score
        self.data = date.today()

    def __repr__(self):
        return f"{self.user_name} {self.score} {self.data}"


Base.metadata.create_all(engine)


def stats_add(score, username):
    Session = sessionmaker(bind=engine)
    session = Session()
    eilute_o = GameBase(username, score)
    session.add(eilute_o)
    session.commit()
    session.close()


def get_stats():
    Session = sessionmaker(bind=engine)
    session = Session()
    top_10 = session.query(GameBase).order_by(GameBase.score.desc())[:10]
    session.close()
    return top_10
