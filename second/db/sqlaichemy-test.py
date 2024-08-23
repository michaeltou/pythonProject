from sqlalchemy import create_engine,  Column,String,Integer

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))


engine = create_engine('mysql+mysqlconnector://root:tm123456@localhost:3306/test')

DBSession = sessionmaker(bind=engine)
session = DBSession()

new_user = User(name='John Doe')

session.add(new_user)

session.commit()
session.close()

