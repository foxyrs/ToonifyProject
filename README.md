## ToonifyProject

# Gide installation du projet

Prérequis :
  1. Installer Python 3.10.2 et s’assurer que Python soit dans le PATH d’environnement de votre machine. Guide installation de python sous windows

Procédure :
  1. Rejoidre le git et cloner le projet
  2. Ouvrir un terminal de commande
  3. Aller dans le dossier `ToonifyProject`et lancer l’environnement virtuel python grâce à la commande suivante : `Scripts\activate.bat` L’environnement Python contient des librairies installées comme « pip » et contient aussi le projet django
  4. (optionnel) Mettre a jour pip
  5. Installer Django `python -m pip install Django`
  6. Vérifier que django est bien en version 4.0.2 grâce à la commande `python -m django --version`
  7. Aller dans le repertoire `ToonifyProject\application` et lancer le serveur local avec la commande `python manage.py runserver`
  9. Aller sur la route http://127.0.0.1:8000/toonifyApp/ J’ai suivi ce tuto pour créer une première page avec le système de routage : [le tuto magique](https://docs.djangoproject.com/fr/4.0/intro/tutorial01/)
