import sys
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Restaurant(Base):
	__tablename__ = 'restaurant'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)

	@property
	def serialize(self):
		return {
		'id': self.id,
		'name': self.name
		}


class MenuItem(Base):
	__tablename__ = 'menu_item'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	description = Column(String(250))
	categorie = Column(String(250))
	price = Column(String(25), nullable=False)
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)

	@property
	def serialize(self):
		return {
		'id': self.id,
		'name': self.name,
		'description': self.description,
		'price': self.price,
		'categorie': self.categorie,
		'restaurant_id': self.restaurant_id
		}




engine = create_engine('sqlite:///restaurants.db')
Base.metadata.create_all(engine)
