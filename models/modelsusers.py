from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# Création de la base de données
Base = declarative_base()

# Déclaration de la table `pays`
class Pays(Base):
    __tablename__ = "pays"
    pays_id = Column(Integer, primary_key=True)
    pays = Column(String(255))

    # Relation inverse avec Users pour accéder aux utilisateurs de chaque pays    
    utilisateurs = relationship('Users', back_populates='pays')

# Déclaration de la table `users`
class Users(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    pays_id = Column(Integer, ForeignKey('pays.pays_id'))

  # Définition de la relation avec la table `Pays`
    pays = relationship('Pays', back_populates='utilisateurs')

# Déclaration de la table `prix`
class Prix(Base):
    __tablename__ = "prix"
    prix_id = Column(Integer, primary_key=True)
    prix = Column(Integer)