'''
Modue to provide the Data acces objects and manipulate the database.

Import this module and then create a new DbSession object to 
manage the transsaction. After that you can use the apropiated class
to perform querys or persisted new or manipulated objects.
'''
from birds.declarative_birds import *

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

# Private property to hold the 
_db_string = 'sqlite:///db/birds.db'

_ENGINE = create_engine(_db_string, echo=True)

Base.metadata.bind = _ENGINE

DbSession = sessionmaker(bind=_ENGINE)

class GenericDao(object):
	'''Provide the common functionalities to DAOs
	To use it must be subclased and overide the default constructor to set the entity class field, example:
		class ModelClassDao(GenericDao):
			def __init__(self):
				ModelClassDao.entity = ModelClass
	Class fields:
	 entity -- stores the Object class to which the operations are going to be performed
	'''
	entity = None

	def save(self, session, persisted_object):
		session.add(persisted_object)

	def delete(self, session, persisted_object):
		session.delete(persisted_object)

	@classmethod
	def get(cls, session, id):
		'''Obtains an object from the database, serched by his id
		Attributes:
			session -- the SqlAlchemy session object
			id -- the unique identifier of the object
		'''
		print(cls)
		print(cls.entity)
		return session.query(cls.entity).get(id)

	@classmethod
	def get_all(cls, session):
		"""Obtains all data from the superior_taxon table
		Attributes:
			session -- the SqlAlchemy session object
		Returns a list with the objects retrieved
		"""
		return session.query(cls.entity).all()

	@classmethod
	def count(cls, session):
		'''Count the total of objects persisted
		 Attributes:
			session -- the SqlAlchemy session object
		 Returns an integer with the total rows founded
		'''
		return session.query(func.count(cls.entity.id)).scalar()

	@classmethod
	def find_by(cls, session, **kwargs):
		'''Find objects by his fields
		You can pass any number of fields in the manner of **kwargs dictionary
		where the key represent the field to look and the value the string to look
		Attriutes:
		 session -- the session in which you want to perform the search.
		 **kwargs -- filters to the search
		'''
		query = session.query(cls.entity)

		for k, v  in kwargs.items():
			filter_value = k + "=" + v
			query.filter(filter_value)
		 
		return query.order_by(cls.entity.id).all()

class SuperiorTaxonDao(GenericDao):
	"""Perform the data acces to the superior_taxon table"""

	def __init__(self):
		SuperiorTaxonDao.entity = SuperiorTaxon

	def get_superior_taxon(self, session, reino, philum, taxon_class):
		"""Find a taxon superior, this should return just one record
		"""
		query = session.query(self.entity).\
			filter(self.entity.reino == reino).\
			filter(self.entity.philum == philum).\
			filter(self.entity.taxon_class == taxon_class)	

		return query.first()

class BirdDao(GenericDao):
	'''Provide the acces to the data for the Bird objects
	'''
	def __init__(self):
		BirdDao.entity = Bird


class VarietyDao(GenericDao):
	'''Data acces object for the Variety
	'''
	def __init__(self):
		VarietyDao.entity = Variety
