from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship

from app.config.extend import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    hashed_password = Column(String)
    role_id = Column(String(32))


# class Address(Base):
#     __tablename__ = 'addresses'
#
#     id = Column(Integer, primary_key=True)
#     email = Column(String, nullable=False)