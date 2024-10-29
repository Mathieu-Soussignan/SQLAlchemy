import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.modelsusers import Base, Users

# Créer l'URL de la base de données en mémoire (ou autre URL si vous avez une base permanente)
DATABASE_URL = "sqlite:///database.sqlite"

# Créer un moteur SQLAlchemy et une session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Afficher une image d'accueil
st.title("Bienvenue sur l'Application de Gestion des Utilisateurs")
st.image("./assets/naruto.jpg", caption="Bienvenue !", use_column_width=True)

# Ajouter un utilisateur
st.header("Ajouter un Utilisateur")
name = st.text_input("Nom de l'utilisateur")
pays_id = st.number_input("Pays ID", min_value=1, step=1)

if st.button("Ajouter l'utilisateur"):
    if name:
        new_user = Users(name=name, pays_id=pays_id)
        session.add(new_user)
        session.commit()
        st.success(f"L'utilisateur {name} a été ajouté avec succès.")
    else:
        st.error("Veuillez entrer un nom.")

# Voir les utilisateurs existants
st.header("Tous les Utilisateurs")
users = session.query(Users).all()
for user in users:
    st.text(f"ID: {user.user_id}, Nom: {user.name}, Pays ID: {user.pays_id}")

# Mettre à jour un utilisateur
st.header("Mettre à Jour un Utilisateur")
update_user_id = st.number_input("ID de l'utilisateur à mettre à jour", min_value=1, step=1)
new_name = st.text_input("Nouveau Nom")

if st.button("Mettre à Jour l'utilisateur"):
    user_to_update = session.query(Users).filter_by(user_id=update_user_id).first()
    if user_to_update:
        user_to_update.name = new_name
        session.commit()
        st.success(f"L'utilisateur avec l'ID {update_user_id} a été mis à jour.")
    else:
        st.error(f"Aucun utilisateur trouvé avec l'ID {update_user_id}.")

# Supprimer un utilisateur
st.header("Supprimer un Utilisateur")
delete_user_id = st.number_input("ID de l'utilisateur à supprimer", min_value=1, step=1)

if st.button("Supprimer l'utilisateur"):
    user_to_delete = session.query(Users).filter_by(user_id=delete_user_id).first()
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()
        st.success(f"L'utilisateur avec l'ID {delete_user_id} a été supprimé.")
    else:
        st.error(f"Aucun utilisateur trouvé avec l'ID {delete_user_id}.")

# Fermer la session à la fin
session.close()