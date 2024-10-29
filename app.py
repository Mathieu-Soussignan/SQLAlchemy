from models.modelsusers import Users, Pays, Prix, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import os

try:
    os.remove('database.sqlite') 
except:
    print("bllaaahhh")


# Déclaration du moteur de base de données
engine = create_engine('sqlite:///database.sqlite')

# Création de la base de données
Base.metadata.create_all(engine)

# Création d'une session
session = Session(bind=engine)
# Création d'un utilisateur
toto = Users(name="toto")
fr = Pays(pays="france")
p1 = Prix(prix=10)

# Insertion de l'utilisateur 
session.add(toto)
session.add(fr)
session.add(p1)
session.commit()