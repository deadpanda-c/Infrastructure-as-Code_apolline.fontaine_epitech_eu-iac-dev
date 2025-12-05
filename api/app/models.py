from sqlalchemy import Column, Integer, String, Boolean
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(50))
    admin = Column(Boolean)
    
    def __init__(self, email, username, password, is_admin):
        self.username = username
        self.email = email
        self.password = password
        self.admin = is_admin
        
    def __repr__(self):
        return '<User %r>' % self.username

