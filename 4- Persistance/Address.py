from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    street_number = Column(String(255))
    street_name = Column(String(255))
    post_code = Column(String(255))
    city = Column(String(255))
    person_id = Column(Integer, ForeignKey('person.id'))