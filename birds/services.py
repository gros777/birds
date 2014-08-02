
'''
Module to provide the bussnes logic for the birds application.


'''
from birds.daos import *
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

import logging


class ServiceError(Exception):
	"""Exception raised for error in the services
	Attributes: 
		message -- explanation of the error
	"""
	message = ""
	def __init__(self, message):
		self.message = message

class SessionSingleton(object):
	'''Class to provide a unique session across all the services
	Methods:
	 get_session() -- class method to retrieve the session
	'''
	_session = None

	def get_session():
		'''Method to retrieve the valid session for the services.
		this returns the same DbSession object between calls.
		'''
		if SessionSingleton._session is None:
			SessionSingleton._session = DbSession()
		return SessionSingleton._session

class SuperiorTaxonService(object):
	_session = None
	_st_dao = None

	def __init__(self):
		if SuperiorTaxonService._session is None:
			self._session = SessionSingleton.get_session()
			SuperiorTaxonService._session = self._session
		self._st_dao = SuperiorTaxonDao()

	def add_superior_taxon(self, superior_taxon):

		superior_taxon_from_db = self._st_dao.\
			get_superior_taxon( self._session, superior_taxon.reino, superior_taxon.philum, superior_taxon.taxon_class)

		if type(superior_taxon_from_db) == type(superior_taxon):
			print(superior_taxon_from_db)
			print (superior_taxon)

			raise ServiceError("The superior Taxon allready exist")

		try:
			self._st_dao.save(self._session, superior_taxon)
			self._session.commit()
		except Exception as e:
			self._session.rollback()
			raise e		

	def delete_superior_taxon(self, superior_taxon):
		try:
			superior_taxon = self._st_dao.get_superior_taxon( self._session, superior_taxon.reino, superior_taxon.philum, superior_taxon.taxon_class)
			print("From Service - delete: ", superior_taxon)
			self._st_dao.delete(self._session, superior_taxon)
			self._session.commit()
		except Exception as e:
			self._session.rollback()
			logging.warning('Error during deleting entity ' + superior_taxon.__rpr__())
			raise e

	def get_by_id(self, taxon_id):
		try:
			return self._get_by_id(taxon_id)
		except ServiceError as e:
			raise e
	
	def _get_by_id(self, taxon_id):
		try:
			return  self._st_dao.get(self._session, taxon_id)
		except MultipleResultsFound as mrf_e:
			raise ServiceError("There was more than one result for the ID, error: " + mrf_e.value)
		except NoResultFound as nrf_e:
			raise ServiceError("There was no result for the ID, error: " + nrf_e.value)
		

	def get_all_superior_taxons(self):

		try:
			return st_dao.get_all(self._session)
		except Exception as e:
			raise ServiceError( e.value )
		

	def count_taxons(self):
		st_dao = SuperiorTaxonDao()
		self._session = DbSession()

		try:
			return st_dao.count(self._session)
		except  Exception as e:
			raise e
		
