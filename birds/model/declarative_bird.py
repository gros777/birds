import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class SuperiorTaxon(Base):
	"""Descrive the objet used to store and manipulate \ 
	   a superior taxon for a bird """

	__tablename__ = 'superior_taxon'

	superior_taxon_id = Column(Integer, primary_key=True)
	reino = Column(String)
	philum = Column(String)
	taxon_class = Column(String)

	def __repr__(self):
		return "<SuperiorTaxon(reino='%s', philum='%s', taxon_class='%s')>" % (
		self.reino, self.philum, self.taxon_class)

class Bird(Base):
	__tablename__ = 'bird'

	bird_id = Column(Integer, primary_key=True)
	order = Column(String)
	family = Column(String)
	genre = Column(String)
	species = Column(String)
	common_name = Column(String)
	bibliography = Column(String)
	superior_taxon_id = Column(Integer, ForeignKey('superior_taxon.superior_taxon_id'))
	superior_taxon = relationship(SuperiorTaxon)

class Variety(Base):
	__tablename__ = 'variety'

	variedad_id = Column(Integer, primary_key=True)
	descripcion = Column(String)
	sighting_place = Column(String)
	sighting_date = Column(Date)
	bird_id = Column(Integer, ForeignKey('bird.bird_id'))
	bird = relationship(Bird)

# engine = create_engine('sqlite:///../../db/birds.db')	

# Base.metadata.create_all(engine)

