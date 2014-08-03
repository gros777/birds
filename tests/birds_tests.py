from nose.tools import *
from birds.services import *
from birds.declarative_birds import SuperiorTaxon

from sqlalchemy.orm.session import Session

import logging

def setup():
    logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
    logging.info('Setup for birds_tests.py')
    print ("SETUP!")
def teardown():
    logging.info('Tear down for birds_tests.py')
    print ("TEAR DOWN!")

def test_superior_taxon_service():
    '''Test for the SuperiorTaxonService class.
    sequece of events:
        1. gets the number of SuperiorTaxon objects persisted in the application
        2. Creates a new SuperiorTaxon object
        3. attempt to persist the new object
        4. gets the number of SuperiorTaxon objects persisted after the add_superior_taxon operation
        5. retrieves the object recient persisted from the session with the id.
        6. erase the persisted object
    '''

    logging.info("\nTEST FOR superior_taxon BEGIN:\n")

    st_service = SuperiorTaxonService()

    logging.info("\nGetting the row count before insertion:\n")
    st_initial_count = st_service.count_taxons();

    logging.info("\nCount before insertion: %d\n", st_initial_count)
    print ("Count before insertion: ", st_initial_count)

    superior_taxon = SuperiorTaxon(reino = 'Animalia', philum = 'NoChordata', taxon_class='Aves')

    logging.info("\nBegining insertion of object: %s\n", superior_taxon)
    st_service.add_superior_taxon(superior_taxon)
    logging.info("\nobject after insertion: %s\n", superior_taxon)

    print(superior_taxon)

    logging.info("\nGetting the row count after insertion:\n")
    st_after_insert_count = st_service.count_taxons();

    logging.info("\nCount after insertion: %s\n", st_after_insert_count)    
    print ("Count after insertion: ", st_after_insert_count)

    assert( (st_after_insert_count - st_initial_count) == 1)

    logging.info("\nGetting the new taxon\n")
    superior_taxon_new = st_service.get_by_id(st_after_insert_count)

    print("new superior taxon : ", superior_taxon_new)

    logging.info("\deleting object registered in the database with id: %d", superior_taxon_new.id)

    st_service.delete_superior_taxon(superior_taxon_new)

    logging.info("\nGetting the row count after deleting\n")
    st_after_delete_count = st_service.count_taxons();

    logging.info("\nrow count after deleting: %d\n", st_after_delete_count)
    print ("Count after delete: ", st_after_delete_count)

    assert( (st_after_delete_count - st_initial_count) == 0)

#@with_setup(setup, teardown)
def test_Service():
    session =  Service.get_session()
    st_service = SuperiorTaxonService()
    logging.info(hex(id(session)))
    logging.info(hex(id(st_service._session)))
    assert(hex(id(session)) == hex(id(st_service._session)))


