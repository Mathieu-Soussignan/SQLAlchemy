### Guide d'Utilisation de SQLite dans le Terminal macOS

Ce guide détaille les actions que vous pouvez réaliser sur une base de données SQLite via le terminal macOS. Cela vous permettra de répondre efficacement aux questions de votre formateur concernant l'utilisation de SQLite pour manipuler et visualiser les données d'une base de données `database.sqlite`. Voici un résumé complet de ce qui a été fait, ainsi que des commandes utilisées.

#### 1. Accéder au Terminal
- Pour ouvrir le terminal sur macOS, appuyez sur `Cmd + Space`, tapez **Terminal**, puis appuyez sur **Entrée**.

#### 2. Naviguer vers le Dossier de votre Projet
- Utilisez la commande `cd` pour changer de répertoire vers celui contenant le fichier **`database.sqlite`** :
  ```bash
  cd /chemin/vers/votre/projet
  ```
  Remplacez **`/chemin/vers/votre/projet`** par le chemin exact où se trouve votre fichier.

#### 3. Ouvrir la Base de Données SQLite
- Une fois dans le bon répertoire, ouvrez la base de données avec la commande suivante :
  ```bash
  sqlite3 database.sqlite
  ```
  Cela lance le shell SQLite et vous permet d'interagir avec la base de données.

#### 4. Tester la Base de Données avec les Commandes SQLite
Voici les principales commandes pour explorer et manipuler les données de votre base de données.

##### 4.1 Voir la Liste des Tables
- Pour lister toutes les tables présentes dans la base de données :
  ```sql
  .tables
  ```
  Cela vous montrera les tables comme **`user`**, **`pays`**, **`prix`**.

##### 4.2 Voir la Structure d'une Table
- Pour voir la structure d'une table précise (par exemple `user`) :
  ```sql
  .schema user
  ```
  Cela montre la structure de la table, incluant les colonnes et leurs types.

##### 4.3 Afficher les Données d'une Table
- Pour afficher tous les enregistrements présents dans la table `user` :
  ```sql
  SELECT * FROM user;
  ```
  Cette commande listera tous les enregistrements de la table `user`.

##### 4.4 Insérer des Données dans une Table
- Pour insérer de nouvelles données dans la table `user` :
  ```sql
  INSERT INTO user (name, pays_id) VALUES ('Itachi', 1);
  ```
  Cela ajoute un utilisateur nommé **Itachi** avec `pays_id` de `1` à la table `user`.

##### 4.5 Mettre à Jour un Enregistrement
- Pour modifier le nom d'un utilisateur dans la table `user` :
  ```sql
  UPDATE user SET name = 'Itachi Uchiha' WHERE name = 'Itachi';
  ```
  Cette commande met à jour le nom **Itachi** pour le remplacer par **Itachi Uchiha**.

##### 4.6 Supprimer un Enregistrement
- Pour supprimer un enregistrement dans la table `user` :
  ```sql
  DELETE FROM user WHERE name = 'Itachi Uchiha';
  ```
  Cela supprime l'utilisateur dont le nom est **Itachi Uchiha**.

##### 4.7 Quitter SQLite
- Pour quitter le shell SQLite et revenir au terminal classique :
  ```sql
  .exit
  ```

### Exemple Complet d'Utilisation
Voici une séquence de commandes que vous pouvez utiliser pour tester et manipuler votre base de données :
1. **Changer de répertoire vers le projet** :
   ```bash
   cd /chemin/vers/votre/projet
   ```
2. **Ouvrir la base de données** :
   ```bash
   sqlite3 database.sqlite
   ```
3. **Lister les tables** :
   ```sql
   .tables
   ```
4. **Voir la structure de la table `user`** :
   ```sql
   .schema user
   ```
5. **Afficher tous les utilisateurs** :
   ```sql
   SELECT * FROM user;
   ```
6. **Ajouter un utilisateur** :
   ```sql
   INSERT INTO user (name, pays_id) VALUES ('Itachi', 1);
   ```
7. **Mettre à jour un utilisateur** :
   ```sql
   UPDATE user SET name = 'Itachi Uchiha' WHERE name = 'Itachi';
   ```
8. **Supprimer un utilisateur** :
   ```sql
   DELETE FROM user WHERE name = 'Itachi Uchiha';
   ```
9. **Quitter SQLite** :
   ```sql
   .exit
   ```

### Conclusion
Avec ces commandes, vous êtes capable d'interagir avec votre base de données SQLite depuis le terminal macOS. Cela vous permet de **tester** la création des tables, de **manipuler** les données (insertion, mise à jour, suppression) et de **visualiser** le contenu de chaque table. Ces actions sont essentielles pour comprendre le fonctionnement d'une base de données et répondre aux questions de votre formateur en toute confiance.