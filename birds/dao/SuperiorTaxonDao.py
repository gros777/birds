from birds.model import Superior_taxon, Base

class SuperiorTaxonDao(object):

	ENGINE = create_engine('sqlite:///../../db/birds.db')


	def get_session(self):
		Base.metadata.bind = ENGINE

		DBSession = sessionmaker(bind=engine)

		return DBSession()

	def save(self, superior_taxon):
		"""Save a new person in the database"""
		if superior_taxon.reino && superior_taxon.philum && superior_taxon.taxon_class:
			session = get_session()


