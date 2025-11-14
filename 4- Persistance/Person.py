from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Address import Address, Base

class Person(Base):

    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    taille = Column(Integer, nullable=False)
    addresses = relationship(Address, backref='person', cascade='all, delete-orphan')