# OC-DJ-P9/ LITReview


***

## 1.Presentation
***
Ceci est une application Web permettant un des utilisateurs inscrits sur le site d'émettre des demandes de critiques de livres ou d'articles et d'y répondre.

## 2-Installation  :
***
Se diriger sur le repertoire où l'on souhaite installer l'application.

Pour installer le programme via un terminal :  

Sous Windows :  
```sh
$ git clone https://github.com/quentin8469/OC-DJ-P9.git    
$ python3 -m venv env  
$ venv/scripts/activate  
$ pip3 install -r requirements.txt   
```
Sous linux/Mac :      
```sh
$ git clone https://github.com/quentin8469/OC-DJ-P9.git   
$ python3 -m venv env    
$ source env/bin/activate    
$ pip3 install -r requirements.txt    
```

**Lancement du serveur Django** :

* Se rendre dans le repertoire contenant le fichier python ' manage.py ' ( litreview )
* Puis exécuter python manage.py runserver
* La page sera accessible à l'URL suivante:  http://127.0.0.1:8000/

## 3- Fonctionnement:

* Suivre l'url: http://127.0.0.1:8000/
* S'inscrire
* S'authentifier
* Créer un ticket ou une critique.
* Suivre un utilisateur existant

## 3- Liste des utilisateurs existants:
* nom: Jean12, mdp:
* nom: Edouard42, mdp:
* nom: Sylvie45, mdp:
* nom: Denis84, mdp:
* nom: Jessica69, mdp:


***
Créer un rapport flake8 :  

`flake8 --exclude=env,venv --format=html --htmldir=flake8_report --max-line-lengt=119`

