## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

#### Variables d'envrionnement 

Une variable d'environnement est nécessaire pour faire fonctionner l'application, à ajouter dans un fichier .env :  

- `DATABASE_URL=sqlite:///oc-lettings-site.sqlite3`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Production

### Prérequis

- Docker installé en local avec un compte hub.docker
- Compte sur circleCI
- heroku installé en local avec un compte sur heroku

### Résumé du fonctionnement

La compilation et les tests se font par l'intermédiaire de circleCI lors du push sur une branche, ils sont parametrés dans .circlci/config.yml. Pour celà l'application circleci doit être relié au dépot github du projet.
Le déploiement se fait sur heroku après un push sur la branche master, si la compilation et les test se sont déroulés avec succés. 

### récupérer une image docker sur le hub

- `docker pull dimitridockerhoareau/oc_lettings_site && docker run -e DATABASE_URL=sqlite:///oc-lettings-site.sqlite3 -p 8000:8000 dimitridockerhoareau/`
Si une migration est nécessaire :
- Récupérer l'id du container :
- `docker ps -a`
- Récupérer l'id du container :
- `docker exec -t -i <id> bash`
- `python manage.py migrate`
- Aller sur localhost:8000 pour lancer l'application

#### Déploiement sur Heroku

- Créer l'application sur heroku :
- `heroku create oc-lettings-974`
- Configurer une BDD postgres pour heroku :
- ` heroku addons:create heroku-postgresql:hobby-dev`
- (Facultatif) Migrer les données de la base de donnée locale en production :
- `heroku run python3 manage.py loaddata whole.json -a oc-lettings-974`


#### Suivi sur Sentry

Ajouter les hash de Sentry dans le fichier .env  
- `SENTRY_KEY=<sentry_url>`
