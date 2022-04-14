"""Création de Yannis Bronnec"""

    
# Pour le plateau de jeux
    
import numpy as np

# Pour l'interface graphique

import pygame

# Pour les préconfiguration de calcul

import math

# Pour sortir de python avec sys.exit() 

import sys



"""-------------------------------------------------------------------------------------"""

    # Définition des couleurs en RVB

BLEU = (49,140,231)
NOIR = (0,0,0)
VERT = (130,196,108)
ORANGE = (255,127,0)

    # On définit le nombre de ligne et colonne

nombre_de_lignes = 6
nombre_de_colonnes = 7


    # Création d'une liste de liste et l'affecte à la variable plateau

def create_board():
    plateau = np.zeros((nombre_de_lignes,nombre_de_colonnes)) 
    return plateau

""" np.zeros permet de créer une liste de liste avec les variables """

    # Permet de choisir à quel endroit mettre le pion

def lacher_piece(plateau, ligne, col, piece):
    plateau[ligne][col] = piece

    # Retire un nombre où le pion attérit 

def si_location_valide(plateau, col):
    return plateau[nombre_de_lignes-1][col] == 0

    # Vérifie si chaque ligne du plateau est = 0 (donc vide)

def obtenir_la_ligne_ouverte_suivante(plateau, col):
    for r in range(nombre_de_lignes):
            if plateau[r][col] == 0:
                        return r

def print_plateau(plateau):
    print(np.flip(plateau, 0))
    
    # On définit tout les mouvements gagnant

def Mouvement_gagnant(plateau, piece):
    
    # Regarde les position horizontale pour la victoire
    
    for c in range(nombre_de_colonnes-3):
            for r in range(nombre_de_lignes):
                        if plateau[r][c] == piece and plateau[r][c+1] == piece and plateau[r][c+2] == piece and plateau[r][c+3] == piece:
                                        return True

	# Regarde les position vertical pour la victoire
    
    for c in range(nombre_de_colonnes):
            for r in range(nombre_de_lignes-3):
                        if plateau[r][c] == piece and plateau[r+1][c] == piece and plateau[r+2][c] == piece and plateau[r+3][c] == piece:
                                        return True
            


	# Regarde les diagonales vers la droite
    
    for c in range(nombre_de_colonnes-3):
            for r in range(nombre_de_lignes-3):
                        if plateau[r][c] == piece and plateau[r+1][c+1] == piece and plateau[r+2][c+2] == piece and plateau[r+3][c+3] == piece:
                                        return True
            


	# Regarde les diagonales vers la gauche
    
    for c in range(nombre_de_colonnes-3):
            for r in range(3, nombre_de_lignes):
                        if plateau[r][c] == piece and plateau[r-1][c+1] == piece and plateau[r-2][c+2] == piece and plateau[r-3][c+3] == piece:
                                        return True
            
             

            
    # On dessine le plateau avec pygame

def dessin_plateau(board):
    for c in range(nombre_de_colonnes):
            for r in range(nombre_de_lignes):
                        pygame.draw.rect(écran, BLEU, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                        pygame.draw.circle(écran, NOIR, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), Rayon)
	
    # Dessin des pions de jeux
    
    for c in range(nombre_de_colonnes):
            for r in range(nombre_de_lignes):		
                        if board[r][c] == 1:
                                        pygame.draw.circle(écran, VERT, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), Rayon)
                        elif board[r][c] == 2: 
                            pygame.draw.circle(écran, ORANGE, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), Rayon)
    pygame.display.update() 

    
""" pygame.display.update permet de mettre à jours l'écran """


# On donne à la variable plateau les propriétes des fonctions

plateau = create_board()
print_plateau(plateau)

# On définit game over en faux et on met les tours à 0

game_over = False
turn = 0

pygame.init() 

""" pygame.INIT permet d'initialiser les modules importé de pygame """

SQUARESIZE = 100 # On définit la taille des carrés

# On met la forme pour chaque endroit du plateau

width = nombre_de_colonnes * SQUARESIZE 
height = (nombre_de_lignes+1) * SQUARESIZE


taille = (width, height) # On définit la taille grace au nombre de case en ligne et en colonne

Rayon = int(SQUARESIZE/2 - 5) # On reduit la taille des cercles pour faire des endroits vides

écran = pygame.display.set_mode(taille) # On définit la taille de la fenetre
dessin_plateau(plateau) # Puis on importe le plateau
pygame.display.update() 

""" pygame.display.update permet de mettre à jours l'écran """

          # Création de la police d'écriture du texte game over 

myfont = pygame.font.SysFont("comic sans ms", 75)

# Tant que la partie n'est pas terminé python execute en permanance ce bout de programme

""" Sys.exit permet de quitter le jeux """

while not game_over:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        sys.exit() 

            if event.type == pygame.MOUSEMOTION : 
                            pygame.draw.rect(écran, NOIR, (0,0, width, SQUARESIZE)) # Dessine le fond
                            posx = event.pos[0]
                            if turn == 0: # Permet de savoir à qui est le tour
                                pygame.draw.circle(écran, VERT, (posx, int(SQUARESIZE/2)), Rayon) # Dessine un pion vert qui suit la souris
                            else: 
                                pygame.draw.circle(écran, ORANGE, (posx, int(SQUARESIZE/2)), Rayon) # Dessine un pion orange qui suit la souris
            pygame.display.update() # Met à jour la frame pour effectuer le changement sur l'écran
        
        

    # Desine le fond si on appuie sur le bouton gauche de la souris

            """ pygame.mousebuttondown déclenche une action lors ce que on appuie sur le bouton gauche de la souris """

            if event.type == pygame.MOUSEBUTTONDOWN: 
                pygame.draw.rect(écran, NOIR, (0,0, width, SQUARESIZE))
			
            
            
			# Demande l'action du joueur 1
            

            
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if si_location_valide(plateau, col): # Vérifie si le placement est valide
                        ligne = obtenir_la_ligne_ouverte_suivante(plateau, col) # Regarde la colonne pour voir ses disponibilités
                        lacher_piece(plateau, ligne, col, 1) # Lache le pion au point vide le plus bas

                        if Mouvement_gagnant(plateau, 1):
                            label = myfont.render("Le joueur 2 a gagné !", 1, VERT) # Affiche la victoire si le joueur aligne 4 pions
                            écran.blit(label, (4,-6))
                            game_over = True


			# Demande l'action du joueur 2
            
            # Math.floor permet de renvoyer des nombres entiers pour choisir une colonne en particulier sans faire un entre deux""" 
            
                else:				
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if si_location_valide(plateau, col):
                        ligne = obtenir_la_ligne_ouverte_suivante(plateau, col)
                        lacher_piece(plateau, ligne, col, 2)

                        if Mouvement_gagnant(plateau, 2):
                            label = myfont.render("Le joueur 2 a gagné !", 1, ORANGE)
                            écran.blit(label, (4,-6)) # écran.blit permet d'afficher le texte contenue dans la variable label en position 4,-6 
                            game_over = True

                print_plateau(plateau)
                dessin_plateau(plateau)

            # Création du nombre de tour pour demander l'action des joueurs
        
                turn += 1 # Rajoute un tour à chaque passage
                turn = turn % 2

            # pygame.time.wait met le programme en pause 

                if game_over:
                    pygame.time.wait(3000)
                
