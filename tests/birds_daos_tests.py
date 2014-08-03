from nose.tools import *
import logging

from birds.daos import *
from birds.declarative_birds import *
from birds.services import Service


def setup():
    logging.basicConfig(filename='test_daos.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
    logging.info('Setup for birds_tests.py')
    global session
    session = Service.get_session()

def teardown():
    logging.info('Tear down for birds_tests.py')
    session.close()

def test_BirdDao():
    '''Test the BirdDao class
    steps:
        1. obtain the superior taxon, 
        2. create a new Bird object
        3. persist the new Bird object
        4. delete the object inserted
    '''
    st_dao = SuperiorTaxonDao()
    st_obj = st_dao.get(session, 1)

    bird_obj = Bird(order="Falconiformes", family='Falconidae',
                    genre='Falco', species='F. peregrinus',
                    common_name='Halcon Peregrino', 
                    bibliography='Wikipedia: http://es.wikipedia.org/wiki/Falco_peregrinus')
    bird_obj.superior_taxon = st_obj

    b_dao = BirdDao()
    b_dao.save(session, bird_obj)
    session.commit()

    logging.info("Bird object stored: %s", bird_obj)

    bird_count = b_dao.count(session)

    bird_obj = b_dao.get(session, bird_count)

    bird_obj.order = "Falconi-informes"

    b_dao.save(session, bird_obj)
    session.flush()

    modified_obj = b_dao.get(session, bird_count)

    logging.info("Modified object stored: %s", modified_obj)

    birds = b_dao.get_all(session)
    for bird in birds:
        logging.info("Bird %d:\n%s", bird.id, bird)

    b_dao.delete(session, modified_obj)
    session.commit()

    
