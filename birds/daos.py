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
	'''Provide the common
	'''
	entity = None

	def save(self, session, persisted_object):
		session.add(persisted_object)

	def delete(self, session, persisted_object):
		session.delete(persisted_object)

	@classmethod
	def get(cls, session, id):
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
		return session.query(func.count(cls.entity.id)).scalar()

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

	def find_by_order(self, session, order):
		'''Find all the birds by his order.
		   Arguments:
		    session -- a DbSession objet in which to perform the query
		    order -- the order string to look for
		'''
		return session.query(self.entity).\
		          filter(self.entity.order == order).\
		          all()

	
