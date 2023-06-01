from sqlalchemy import Boolean, Column, Enum, Integer, String,Float

from .database import Base
from .schemas import Roles

    
class Book(Base):
    __tablename__ ="book"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    author = Column(String)
    title = Column(String)
    description = Column(String)
    price=Column(Integer)

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True,  autoincrement=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=False)
    role = Column(Enum(Roles), default="user")