# 3 Containers Application
 Application de NLP qui évalue la similarité entre deux phrases.

## Description
Ce projet est une application basée sur des microservices pour évaluer la similarité des phrases en utilisant des techniques de traitement du langage naturel (NLP) et d'apprentissage automatique (ML). Il utilise la conteneurisation Docker pour un déploiement modulaire.

## Composants
- `app/` : Contient l'application web Flask pour gérer les requêtes (`app.py`), les modèles ML (`models.py`), et les dépendances (`requirements.txt`).
- `data/` : Gère le prétraitement des données et les interactions avec la base de données (`data.py`).
- `Dockerfile` : Utilisé pour construire les images Docker pour les services app et data.
- `docker-compose.yml` : Orchestre la configuration multi-conteneurs Docker.

## Démarrage rapide
1. Clonez le dépôt.
2. Naviguez vers le répertoire du dépôt.
3. Exécutez `docker-compose up` pour démarrer les services.

## Services
- **Application Web** : Construite avec Flask, fournissant une interface utilisateur pour saisir les phrases et afficher les résultats de similarité.
- **Service de Données** : Traite le prétraitement des phrases et les interactions avec la base de données.
- **Service de Modèle ML** : Calcule la similarité entre les phrases en utilisant des modèles pré-entraînés.

## Utilisation
- Entrez deux phrases pour évaluer leur similarité.
- Consultez les requêtes précédentes et leurs scores de similarité calculés.
