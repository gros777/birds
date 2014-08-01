
'''
Module to provide the bussnes logic for the birds application.


'''
from birds_daos import *
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound


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
		session = DbSession()

		superior_taxon_from_db = superior_taxon_dao.\
			get_superior_taxon( session,
				superior_taxon.reino,
				superior_taxon.philum,
				superior_taxon.taxon_class)

		if type(superior_taxon_from_db) == type(superior_taxon):
			print(superior_taxon_from_db)
			print (superior_taxon)
			session.close()
			raise ServiceError("The superior Taxon allready exist")

		try:
			superior_taxon_dao.save(session, superior_taxon)
			session.commit()
		except Exception as e:
			session.rollback()
			raise ServiceError("Cannot save the new superior taxon, error: " + e.value)
		finally:
			session.close()

	def get_by_id(self, taxon_id):
		st_dao = SuperiorTaxonDao()
		session = DbSession()

		try:
			return st_dao.get(session, taxon_id)
		except MultipleResultsFound as mrf_e:
			raise ServiceError("There was more than one result for the ID, error: " + mrf_e.value)
		except NoResultFound as nrf_e:
			raise ServiceError("There was no result for the ID, error: " + nrf_e.value)
		finally:
			session.close()

	def get_all_superior_taxons(self):
		st_dao = SuperiorTaxonDao()
		session = DbSession()

		try:
			return st_dao.get_all(session)
		except Exception as e:
			raise ServiceError( e.value )
		finally:
			session.close()
