'''
Modue to provide the Data acces objects and manipulate the database.

Import this module and then create a new DbSession object to 
manage the transsaction. After that you can use the apropiated class
to perform querys or persisted new or manipulated objects.
'''
from birds.declarative_birds import SuperiorTaxon, Base

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

# Private property to hold the 
_db_string = 'sqlite:///db/birds.db'

_ENGINE = create_engine(_db_string, echo=True)

Base.metadata.bind = _ENGINE

DbSession = sessionmaker(bind=_ENGINE)

class GenericDao(object):

	def save(self, session, persisted_object):
		session.add(persisted_object)
		
	def delete(self, session, persisted_object):
		session.delete(persisted_object)

class SuperiorTaxonDao(GenericDao):
	"""Perform the data acces to the superior_taxon table"""

	def get_superior_taxon(self, session, reino, philum, taxon_class):
		"""Find a taxon superior, this should return just one record
		"""
		query = session.query(SuperiorTaxon).\
			filter(SuperiorTaxon.reino == reino).\
			filter(SuperiorTaxon.philum == philum).\
			filter(SuperiorTaxon.taxon_class == taxon_class)	

		return query.first()

	def get(self, session, superior_taxon_id):
		"""
		Retrieve the persisted object by id

		Attributes:
			session -- the SqlAlchemy session object
			id -- the id of the required object as an integer 
		"""

		query = session.query(SuperiorTaxon).\
				filter(SuperiorTaxon.superior_taxon_id == superior_taxon_id)

		return query.one()

	def get_all(self, session):
		"""Obtains all data from the superior_taxon table
		Attributes:
			session -- the SqlAlchemy session object
		Returns a list with the objects retrieved
		"""
		return session.query(SuperiorTaxon).all()

	def count(self, session):
		return session.query(func.count(SuperiorTaxon.superior_taxon_id)).scalar()
