from birds_services import *
from declarative_birds import SuperiorTaxon

st_service = SuperiorTaxonService()

superior_taxon = SuperiorTaxon(reino = 'Animalia', philum = 'Aguatia', taxon_class='Aves')

st_service.add_superior_taxon(superior_taxon)

superior_taxon = st_service.get_by_id(1)

print(superior_taxon)

print(st_service.get_all_superior_taxons())

# from service.birds_services import *

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker


# engine = create_engine('sqlite:///../db/birds.db', echo=True)	

# Base.metadata.create_all(engine)
# Base.metadata.bind = engine

# DBSession = sessionmaker(bind=engine)

# session = DBSession()

# superior_taxon = SuperiorTaxon(reino = 'Animalia', philum = 'Chordata', taxon_class='Aves')
# #superior_taxon. 
# #superior_taxon.
# #superior_taxon.taxon_class='Aves'

# session.add(superior_taxon)

# session.commit()

# aves_superior_taxon = session.query(SuperiorTaxon).filter_by(reino='Animalia').first()

# print (aves_superior_taxon)



