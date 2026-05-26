from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String
)
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class DecisionDB(Base):
    __tablename__ = "decisions"

    id = Column(Integer, primary_key=True)

    decision_number = Column(String)
    decision_date = Column(String)
    case_number = Column(String)
    location = Column(String)
    judge = Column(String)
    source_file = Column(String)


engine = create_engine("sqlite:///decisions.db")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)