#Jaymie Johnston
#Enhancement 1 - System Engineering & Design
#Table for user database
from sqlalchemy import Column, Integer, String
from usersdb import Base

#table for users
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    hashed_password = Column(String(100))
