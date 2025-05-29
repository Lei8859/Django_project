# Django_project
## This is a test project
## Use miniforge to create a virtual environment
- install miniforge [miniforge_link](https://conda-forge.org/download/).
## Use pip to install django

## Essentiel commands conda
- conda env list
- Mettre à jour conda: conda update conda
- Créer un nouvel environnement: conda create -n mon_env python=3.10
- Activer un environnement: conda activate mon_env
- Désactiver un environnement: conda deactivate
- Supprimer un environnement: conda remove --name mon_env --all
- Installer un paquet: conda install numpy
- Lister les paquets installés dans l’environnement actif: conda list
- Créer un environnement à partir d’un fichier YAML: conda env create -f environnement.yaml
- Exporter un environnement (fichier YAML): conda env export > environnement.yaml

## Essentiel command django-admin
django-admin startproject monsite:	Crée un nouveau projet Django nommé monsite
django-admin startapp monapp	Crée une nouvelle application Django dans le projet
django-admin runserver	Démarre un serveur de développement local
django-admin makemigrations	Crée des fichiers de migration à partir des changements dans les modèles
django-admin migrate	Applique les migrations à la base de données
django-admin createsuperuser	Crée un compte administrateur pour le site d’admin
django-admin shell	Lance un shell Python avec le contexte Django chargé
django-admin check	Vérifie le projet pour détecter des erreurs potentielles
