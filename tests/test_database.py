import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.modelsusers import Base, Users

# Configuration pour la base de données en mémoire
DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture
def session():
    # Création du moteur pour la base de données en mémoire
    engine = create_engine(DATABASE_URL)
    # On crée les tables
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session = Session()

    yield Session
    # Fermeture des que les tests sont terminés
    Session.close()
    engine.dispose()

def test_add_user(session):
    # On ajoute un nouvel utilisateur
    add_user = Users(name="Itachi", pays_id=1)
    session.add(add_user)
    session.commit()

    user = session.query(Users).filter_by(name="Itachi").first()
    assert user is not None
    assert user.name == "Itachi"


def test_update_user(session):
    user = Users(name="Naruto", pays_id=1)
    session.add(user)
    session.commit()

    user.name = "Naruto Uzumaki"
    session.commit()

    user_update = session.query(Users).filter_by(name="Naruto Uzumaki").first()
    assert user_update is not None
    assert user_update.name == "Naruto Uzumaki"

def test_delete_user(session):
    user = Users(name="Sasuke", pays_id=1)
    session.add(user)
    session.commit()

    # Suppression de l'utilisateur
    session.delete(user)
    session.commit()

    # Vérification de la suppression
    user_delete = session.query(Users).filter_by(name="Sasuke").first()
    assert user_delete is None




