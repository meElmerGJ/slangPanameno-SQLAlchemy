from sqlalchemy import Column, String, Integer
from base import Base


class SlangPanameno(Base):
    __tablename__ = "slangs"

    id = Column(Integer(), primary_key=True)
    word = Column(String(50), nullable=False, unique=True)
    meaning = Column(String(50), nullable=False)

    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
