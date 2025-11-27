# Projet SGBD

## MongoDB

![MongoDB Logo](./db_logo.jpg)

### Introduction :

Dans le cadre de ce projet, nous présentons un script Python permettant d’établir une connexion avec une base de données MongoDB afin d’effectuer plusieurs opérations fondamentales : l’insertion, la récupération, la mise à jour et la suppression de données.
L’ensemble de ces opérations sera évalué sur deux environnements distincts : une base de données locale et une instance MongoDB dans le cloud `MongoDB Atlas`.

### Prérequis

Pour exécuter ce script, il est nécessaire de disposer des éléments suivants :

- Python, version 3 ;
- MongoDB.

Par la suite, l’installation de la bibliothèque du driver MongoDB peut être effectuée à l’aide de la commande :
`pip install pymongo`

### Exécution du script

Dans le répertoire du projet, le script peut être lancé à l’aide de la commande suivante :
`python3 main.py`

Une fois exécuté, le script vous invite d’abord à choisir entre l’utilisation d’une instance MongoDB locale ou hébergée dans le cloud. Il affiche ensuite l’ensemble des opérations qui seront réalisées. Il suffit alors d’appuyer sur la touche Entrée pour poursuivre l’exécution.

[Voir le script Python](https://github.com/khalil-gharbi-fsb/projet-sgbd/blob/main/main.py)
