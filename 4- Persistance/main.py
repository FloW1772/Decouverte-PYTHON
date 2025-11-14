from random import randint

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, func
from Person import Person
from Address import Address, Base

engine = create_engine('sqlite:///my_db.db')
Base.metadata.bind = engine
Base.metadata.create_all(engine)

DbSession = sessionmaker(bind=engine)
session = DbSession()

new_person = Person(name='Paul', taille=randint(120, 200))
new_address = Address(street_number=1234, street_name='rue des fous', post_code='1234', city='Paris', person = new_person)
session.add(new_address)
session.commit()

person = session.get(Person, 1)
session.delete(person)
session.commit()

# exemple de valeurs scalaires aggrégées
moyennes = session.query(func.avg(Person.taille).label('moyenne_taille')).scalar()

print("Les Paul font en moyenne:",moyennes, 'cm')

print('{} habite au {} {} {} {}'.format(person.name, person.addresses[0].street_number, person.addresses[0].street_name, person.addresses[0].post_code, person.addresses[0].city))