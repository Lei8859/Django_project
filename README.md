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

## Essentiel command django-admin and python manage.py
django-admin startproject monsite   (identique)	                            Crée un nouveau projet Django
django-admin startapp monapp	    python manage.py startapp monapp	    Crée une nouvelle application
django-admin runserver	            python manage.py runserver	            Lance le serveur de développement
django-admin makemigrations	        python manage.py makemigrations	        Génère les fichiers de migration
django-admin migrate	            python manage.py migrate	            Applique les migrations à la base de données
django-admin createsuperuser	    python manage.py createsuperuser	    Crée un compte administrateur
django-admin shell	                python manage.py shell	                Ouvre une console Python avec Django chargé
django-admin check	                python manage.py check	                Vérifie le projet pour détecter des erreurs
django-admin test	                python manage.py test	                Exécute les tests unitaires
django-admin loaddata fichier.json	python manage.py loaddata fichier.json	Charge des données dans la base
django-admin dumpdata	            python manage.py dumpdata	            Exporte les données sous forme JSON
