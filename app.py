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

# Ajouter des pays
pays_france = Pays(pays="France")
pays_espagne = Pays(pays="Espagne")

# Ajouter des utilisateurs
utilisateur_1 = Users(name="Sasuke", pays=pays_france)
utilisateur_2 = Users(name="Naruto", pays=pays_espagne)

# Ajouter les objets à la session
session.add(pays_france)
session.add(pays_espagne)
session.add(utilisateur_1)
session.add(utilisateur_2)

# Sauvegarder les modifications
session.commit()

# Lire tous les utilisateurs avec leurs pays
utilisateurs = session.query(Users).all()
for utilisateur in utilisateurs:
    print(f"Nom : {utilisateur.name}, Pays : {utilisateur.pays.pays}")

# Fermer la session après utilisation
session.close()