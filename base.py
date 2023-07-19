from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# USING PORT 3307 <<<<-----------------------------------
engine = create_engine("mariadb+mariadbconnector://root:248625@localhost:3307/slangpanameno")
Session = sessionmaker(bind=engine)
Base = declarative_base()
