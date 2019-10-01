# masterSDIN

## Installation

- Installer les différents modules utilisés dans les programmes (notamment tweepy et wordcloud)

- `pip install [nom du module]

## Définition des programmes

### Jeu du pendu (VF)

Ceci est un jeu du pendu, il y a 6 lettres et 6 chances. Le programme affiche un " _ _ _ _ _ _" et demande "choisit une lettre".
Nous répondons une lettre x Si cette lettre est dans le mot, il affiche la lettre à la place correspondante et affiche "choisit une nouvelle lettre". Si x n'est pas dans le mot, le programme affiche "perdu, encore n chances. 

Si le bon mot est trouvé avant la fin, le programme affiche "tu as gagné". Autrement, il affichera "GAME OVER".

Démarrer le script `PenduVF.py` pour lancer le jeu.


### Récolte de données Twitter - Autoconsommation

Extrait différents tweets avec les termes "autoconsommation" et le hashtag "#autoconsommation". L'objectif est de collecter un ensemble de données et de réaliser une étude sur les différents résultats obtenus pour ces termes. Le programme va collecter les informations suivantes pour chaque tweet identifié :

* L'ID du Tweet ;
* Le texte du Tweet ;
* Le nombre de Retweet du Tweet ;
* Le nombre de likes du Tweet ;
* La date du Tweet ;
* Les hashtags utilisés dans le Tweet ;
* Les mentions du Tweet ;
* Les coordonnées du Tweet ;
* Le screenname de l'auteur du Tweet ;
* Le nom de l'auteur du Tweet ;
* L'ID de l'auteur du Tweet ;
* La langue de l'auteur du Tweet ;
* La localisation de l'auteur du Tweet ;
* Le nombre de followers de l'auteur du Tweet ;
* Le nombre d'abonnements de l'auteur du Tweet ;


Démarrer le script `scrap twitter autoconsommation.py` pour extraire les informations.

### Nuage de mots

Permet de réaliser un nuage de mot avec les tweets collectées à l'aide du programme précédent.
Pour lancer ce programme, les éléments suivants sont nécessaires

* Télécharger le module nltk ;
* Télécharger le module wordcloud ;
* Télécharger une image en format png avec la forme souhaitée pour le nuage de mot ;
* Définir la langue des STOPWORDS (en fonction des données utilisées pour le nuage de mot) ;
* Définir la colonne correspondante du fichier csv. ;

Démarrer le script `Word_cloud.py` pour réaliser le nuage de mots.

