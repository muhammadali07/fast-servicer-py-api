from sqlalchemy import Column, String, BigInteger, Text, DateTime
from datetime import datetime


class Users(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    email = Column(String(50))
    password = Column(Text)
    role = Column(String(5))
    create_at = Column(DateTime, default=datetime.now())
    