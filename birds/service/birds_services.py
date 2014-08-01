from dao.birds_daos import *


class ServiceError(Exception):
	"""Exception raised for error in the services
	Attributes: 
		message -- explanation of the error
	"""
	message = ""
	def __init__(self, message):
		self.message = message

class SuperiorTaxonService(object):

	def add_superior_taxon(self, superior_taxon):

		superior_taxon_dao = SuperiorTaxonDao()
		session = DBSession()

		superior_taxon_from_db = superior_taxon_dao.\
			get_superior_taxon( session,
				superior_taxon.reino,
				superior_taxon.philum,
				superior_taxon.taxon_class)

		if superior_taxon is not None:
			raise ServiceError("The superior Taxon allready exist")

		try:
			superior_taxon_dao.save(session, superior_taxon)
			session.commit()
		except Exception as e:
			session.rollback()
			raise ServiceError("Cannot save the new superior taxation, error: " + e.value)
		finally:
			session.close()
