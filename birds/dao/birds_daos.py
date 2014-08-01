from model.declarative_bird import SuperiorTaxon, Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

_db_string = 'sqlite:////Users/victor/MyProjects/pythonLearning/birds/db/birds.db'
ENGINE = create_engine(_db_string, echo=True)

Base.metadata.bind = ENGINE

DBSession = sessionmaker(bind=ENGINE)


class SuperiorTaxonDao(GenericDao):
	"""Perform the data acces to the superior_taxon table"""

	def save(self, session, superior_taxon):
		"""Persist a new superior taxon in the database

		Attributes:
		session -- the SqlAlchemy session to work
		superior_taxon -- the new object to persist.
		"""
		if isinstance(superior_taxon.reino, str) \
		   and isinstance(superior_taxon.philum, str) \
		   and isinstance(superior_taxon.taxon_class, str):

			session.add(superior_taxon)
		else:
			raise
	def get_superior_taxon(self, session, reino, philum, taxon_class):
		"""Find a taxon superior, this should return just one record
		"""
		query = session.query(SuperiorTaxon).\
			filter(SuperiorTaxon.reino == reino).\
			filter(SuperiorTaxon.philum == philum).\
			filter(SuperiorTaxon.taxon_class == taxon_class)	

		return query.all()

	def get(self, session, id):
		"""
		"""

		query = session.query(SuperiorTaxon).\
				filter(SuperiorTaxon.superior_taxon_id = id)

		return query.one()
