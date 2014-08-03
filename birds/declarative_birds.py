'''
Module that provide the Model objects for the birds application.

This module use the SqlAlchemy ORM library to work properly.
In this module youll find the classes: SuperiorTaxon, Bird and Variety; each and everyone
are subclases from sqlalchemy.ext.declarative.Base

'''
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()


class SuperiorTaxon(Base):
	"""Descrive the objet used to store and manipulate superior taxons \ 
		To create a new object you jus have to call the \
		constructor with all the members:
		Example:
			new_superior_taxon = SuperiorTaxon(reino = 'Animal', \
												philum = 'philum = 'Chordata', \
												taxon_class='Aves')
		Object Attributes:
			id -- the unique identifier of the object as integer
			reino -- string 
			philum -- string
			taxon_class -- string
	 """

	__tablename__ = 'superior_taxon'

	id = Column(Integer, primary_key=True)
	reino = Column(String)
	philum = Column(String)
	taxon_class = Column(String)
	birds = relationship("Bird", backref='superior_taxon', cascade='all, delete, delete-orphan')

	def __repr__(self):
		return "<SuperiorTaxon(id='%d', reino='%s', philum='%s', taxon_class='%s')>" % (
		-1 if self.id is None else self.id, self.reino, self.philum, self.taxon_class)

class Bird(Base):
	'''Represent a bird object in the application
		Object Attributes:
			id -- the unique identifier as a number
			order -- the oder of the Animal as a string
			family -- string that represent the family of the animal
			genre -- string with the genry
			species -- str with the species
			common_name -- str with the name as he humans know it
			bibliography -- str where it gets the information for this animal
			superior_taxon_id -- SuperiorTaxon object in which this animal is classified
	'''
	__tablename__ = 'bird'

	id = Column(Integer, primary_key=True)
	order = Column(String)
	family = Column(String)
	genre = Column(String)
	species = Column(String)
	common_name = Column(String)
	bibliography = Column(String)
	superior_taxon_id = Column(Integer, ForeignKey('superior_taxon.id'))
	varieties = relationship("Variety", backref='bird', cascade='all, delete, delete-orphan')
	
	def __repr__(self):
		return  (self.superior_taxon.__repr__() +
		    "\n\t<Bird(id=%d, order=%s, family=%s, genre=%s, species=%s, \
			common_name=%s, bibliography=%s>" % (-1 if self.id is None else self.id,
			self.order, self.family, self.genre, self.species, self.common_name,
			self.bibliography))

class Variety(Base):
	__tablename__ = 'variety'

	id = Column(Integer, primary_key=True)
	image = Column(BLOB)
	descripcion = Column(String)
	sighting_place = Column(String)
	sighting_date = Column(Date)
	bird_id = Column(Integer, ForeignKey('bird.id'))
#	bird = relationship(Bird, backref=backref('varieties', order_by=id))

# engine = create_engine('sqlite:///../../db/birds.db')	

# Base.metadata.create_all(engine)

