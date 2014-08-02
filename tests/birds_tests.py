from nose.tools import *
from birds.services import *
from birds.declarative_birds import SuperiorTaxon

def setup():
    print ("SETUP!")
def teardown():
    print ("TEAR DOWN!")
def test_superior_taxon_service():
    st_service = SuperiorTaxonService()

    st_initial_count = st_service.count_taxons();
    print ("Count before insertion: ", st_initial_count)

    superior_taxon = SuperiorTaxon(reino = 'Animalia', philum = 'NoChordata', taxon_class='Aves')

    st_service.add_superior_taxon(superior_taxon)

    print(superior_taxon)

    st_after_insert_count = st_service.count_taxons();    
    print ("Count after insertion: ", st_after_insert_count)
    assert( (st_after_insert_count - st_initial_count) == 1)

    superior_taxon_new = st_service.get_by_id(st_after_insert_count)

    print("new superior taxon : ", superior_taxon_new)

    st_service.delete_superior_taxon(superior_taxon_new)

    st_after_delete_count = st_service.count_taxons();

    print ("Count after delete: ", st_after_delete_count)

    assert( (st_after_delete_count - st_initial_count) == 0)
