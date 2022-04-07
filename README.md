Voici mon projet python : Puissance 4

Pour commencer une partie de puissance 4, on désigne le premier joueur. Celui ci met un de ses jetons de couleur dans l’une des colonnes de son choix. Le jeton tombe alors en bas de la colonne.

Le deuxième joueur insère à son tour son jeton, de l’autre couleur dans la colonne de son choix. Et ainsi de suite jusqu’à obtenir une rangée de 4 jetons de même couleur.

Pour gagner une partie de puissance 4, il suffit d’être le premier à aligner 4 jetons de sa couleur horizontalement, verticalement et diagonalement.

Si lors d’une partie, tous les jetons sont joués sans qu’il y est d’alignement de jetons, la partie est déclaré nulle.

__________________________________________________________________________________________________________________________________________________________

Décomposition en sous problème :

Création du plateau de jeux
Création des pions de jeux
Vérifier la position des pions verticalement, horizontalement et diagonalement
création de l'écran game over pour le joueur 1 et 2
Demande au joueur de placer son pions

Liste de liste

__________________________________________________________________________________________________________________________________________________________

Minimum viable Product :

Création d'un plateau de jeux avec des listes de liste, pourvoir réperer quand 4 pions sont alligné de quelconque facon, mais egalement faire un système de tour pour demander à chaque joueur à la suite de poser son pion pour que celui ci tombe en bas

pour cela je vais utiliser les fonctions : NP.zeros de la bibliothèque numpy afin de créer une liste de liste, mais aussi de la l'affection de nombre à une variable à chaque tour avec "+=", 

