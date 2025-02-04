import pygame
from pygame import *
import copy
from Constante import *

# Pour la classe Selection
selection_en_jeu = Selection.En_Jeu
selection_nouveau_jeu = Selection.Nouveau_Jeu
selection_fin_jeu = Selection.Fin_Jeu

# Pour la classe Nouveau_Debut_Jeu
vie_init = Nouveau_Debut_Jeu.Vie_Init
x_debut_jeu = Nouveau_Debut_Jeu.X_Debut_Jeu
y_debut = Nouveau_Debut_Jeu.Y_Debut_Jeu
y_raquette_debut = Nouveau_Debut_Jeu.Y_Raquette_Debut
vitesse_raquette_debut = Nouveau_Debut_Jeu.Vitesse_Raquette_Debut
x_balle_debut = Nouveau_Debut_Jeu.X_Balle_Debut
y_balle_debut = Nouveau_Debut_Jeu.Y_Balle_Debut
brique_comptes_init = Nouveau_Debut_Jeu.brique_comptes_init

# Pour la classe LimiteJeu
x_raquette = LimiteJeu.X_Raquette
y_lim_balle = LimiteJeu.Y_Lim_balle

pygame.init()

#FENETRE
fenetre = pygame.display.set_mode((taille))

###TEXTE
police = pygame.font.Font(None, 45)
#jouer
texte_debut = police.render("JOUER",1,NOIR)
#stop
texte_stop = police.render("FERMER",1,NOIR)
#rejouer
texte_encore = police.render("ENCORE",1,NOIR)
#scores
texte_score = police.render(texte_str_score,1,NOIR)
#vie
texte_vie_restante = police.render(texte_str_vie_restante,1,NOIR)
#information de jeu
texte_info = police.render("utiliser <- -> et la touche entrer pour selectionner",1,NOIR)
#Gagner
texte_gagner = police.render("GAGNER",1,NOIR)
#Perdu
texte_perdu = police.render("PERDU",1,NOIR)

###PHASE DE JEU
lancer = True
#debut du jeu selection
jeu_selection_debut = True
#jeu
jeu_lancer = False
#arret de jeu
mort = False
gagner = False
#choix
selection = 0
#debut du mouvement de la balle
Lancement = False

while lancer:
    for event in pygame.event.get():
        if event.type == QUIT:
            lancer = False

###ALGORITHME

    if jeu_selection_debut:

        #deplacement de la selection
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                selection = selection_nouveau_jeu
                debut_couleur = ORANGE
                stop_couleur = JAUNE

            if event.key == K_RIGHT:
                selection = selection_fin_jeu
                debut_couleur = JAUNE
                stop_couleur = ORANGE

            #changement de mode de jeu
            if selection == selection_nouveau_jeu and event.key == K_RETURN:
                jeu_selection_debut = False
                jeu_lancer = True
                selection = selection_en_jeu

            if selection == selection_fin_jeu and event.key == K_RETURN:
                lancer = False

    if mort :

        #deplacement de la selection
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                selection = selection_nouveau_jeu
                encore_couleur = ORANGE
                stop_couleur = JAUNE

            if event.key == K_RIGHT:
                selection = selection_fin_jeu
                encore_couleur = JAUNE
                stop_couleur = ORANGE

            #changement de mode de jeu
            if selection == selection_nouveau_jeu and event.key == K_RETURN:
                mort = False
                jeu_lancer = True
                selection = selection_en_jeu
                vie = vie_init
                X_debut = x_debut_jeu
                X_fin = y_debut + x_debut_jeu
                Y_raquette = y_raquette_debut
                vitesses_raquette = vitesse_raquette_debut
                X_balle = x_balle_debut
                Y_balle = y_balle_debut
                brique_compte = brique_comptes_init
                mur_brique = copy.deepcopy(copie_brique)

            if selection == selection_fin_jeu and event.key == K_RETURN:
                lancer = False

    if gagner :

        #deplacement de la selection
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                selection = selection_nouveau_jeu
                encore_couleur = ORANGE
                stop_couleur = JAUNE

            if event.key == K_RIGHT:
                selection = selection_fin_jeu
                encore_couleur = JAUNE
                stop_couleur = ORANGE

            #changement de mode de jeu
            if selection == selection_nouveau_jeu and event.key == K_RETURN:
                gagner = False
                jeu_lancer = True
                selection = selection_en_jeu
                vie = vie_init
                X_debut = x_debut_jeu
                X_fin = y_debut + x_debut_jeu
                Y_raquette = y_Raquette_Debut
                vitesses_raquette = vitesse_raquette_debut
                X_balle = x_balle_debut
                Y_balle = y_balle_debut
                brique_compte = brique_comptes_init
                mur_brique = copy.deepcopy(copie_brique)

            if selection == selection_fin_jeu and event.key == K_RETURN:
                lancer = False

    if jeu_lancer:
        
        if event.type == KEYDOWN:  # déplacement de la raquette
            if event.key == K_LEFT and X_debut > x_raquette:
                X_debut -= vitesses_raquette
                X_fin -= vitesses_raquette
                Lancement = True

            if event.key == K_RIGHT and X_fin < longueur:
                X_debut += vitesses_raquette
                X_fin += vitesses_raquette
                Lancement = True

        if Lancement:

            #Pertes de points
            if Y_balle + diamete_balle > y_lim_balle :
                vie = decrementer(vie)
                X_balle = x_balle_debut
                Y_balle = y_balle_debut
                Lancement = False
                Y_raquette = Y_raquette_copy
                X_debut = X_debut_copy
                X_fin = X_fin_copy
                X_sens = dir_aleatoire()
                Y_sens = dir_aleatoire()
                Vitesse_balle_X = Vitesse_balle_X * X_sens
                Vitesse_balle_Y = Vitesse_balle_Y * Y_sens

            if vie < 1 :
                mort = True
                jeu_lancer = False
                Lancement = False
                Y_raquette = Y_raquette_copy
                X_debut = X_debut_copy
                X_fin = X_fin_copy
                X_sens = dir_aleatoire()
                Y_sens = dir_aleatoire()
                Vitesse_balle_X = Vitesse_balle_X * X_sens
                Vitesse_balle_Y = Vitesse_balle_Y * Y_sens

            if brique_compte == brique_compte_max :
                jeu_lancer = False
                gagner = True
                Lancement = False
                Y_raquette = Y_raquette_copy
                X_debut = X_debut_copy
                X_fin = X_fin_copy
                X_sens = dir_aleatoire()
                Y_sens = dir_aleatoire()
                Vitesse_balle_X = Vitesse_balle_X * X_sens
                Vitesse_balle_Y = Vitesse_balle_Y * Y_sens

            # Mouvement de la balle avec les murs
            if Y_balle < 0 or Y_balle + diamete_balle > longueur:
                Vitesse_balle_Y = -Vitesse_balle_Y

            if X_balle < 0 or X_balle + diamete_balle > largeur:
                Vitesse_balle_X = -Vitesse_balle_X

            # Collision avec la raquette
            if(
                (Y_balle > Y_raquette or
                Y_balle + diamete_balle > Y_raquette or
                Y_balle + diamete_balle > Y_raquette + epaiseur_raquette or
                Y_balle + diamete_balle > Y_raquette + epaiseur_raquette )
                and 
                (X_debut < X_balle + diamete_balle < X_fin or 
                X_debut < X_balle< X_fin )
            ):
                Vitesse_balle_Y = -Vitesse_balle_Y

            for cote in range(epaiseur_raquette):
                if ((
                    (Y_balle > Y_raquette + cote or 
                    Y_balle + diamete_balle > Y_raquette + cote) and
                    (X_fin > X_balle > X_debut or 
                    X_fin > X_balle + diamete_balle > X_debut))
                ):
                    Vitesse_balle_Y = -Vitesse_balle_Y


            # Collision avec les briques

            for (colone, ligne, X, Y) in (

                #ligne 1
                (0, 0, X_brique_1, Y_brique_1),
                (0, 1, X_brique_2 ,Y_brique_1),
                (0, 2, X_brique_3 ,Y_brique_1),
                (0, 3, X_brique_4 ,Y_brique_1),
                (0, 4, X_brique_5 ,Y_brique_1),

                #ligne 2
                (1, 0, X_brique_1 ,Y_brique_2),
                (1, 1, X_brique_2 ,Y_brique_2),
                (1, 2, X_brique_3 ,Y_brique_2),
                (1, 3, X_brique_4 ,Y_brique_2),
                (1, 4, X_brique_5 ,Y_brique_2),

                #ligne 3
                (2, 0, X_brique_1 ,Y_brique_3),
                (2, 1, X_brique_2 ,Y_brique_3),
                (2, 2, X_brique_3 ,Y_brique_3),
                (2, 3, X_brique_4 ,Y_brique_3),
                (2, 4, X_brique_5 ,Y_brique_3),

            ):
                if mur_brique[colone][ligne] != BLEU_FONCE:
                    if (
                        (Y <Y_balle < Y + longeur_brique or 
                        Y <Y_balle < Y or
                        Y <Y_balle + diamete_balle < Y + longeur_brique or
                        Y <Y_balle + diamete_balle < Y)
                        and 
                        (X< X_balle < X + largeur_brique or
                        X< X_balle < X or 
                        X< X_balle + diamete_balle < X or
                        X< X_balle + diamete_balle < X + largeur_brique)
                        ):

                        if mur_brique[colone][ligne] == JAUNE:
                            Vitesse_balle_Y = -Vitesse_balle_Y
                            mur_brique[colone][ligne] = BLEU_FONCE
                            brique_compte += point_par_brique
                            break

                        if mur_brique[colone][ligne] == ORANGE:
                            Vitesse_balle_Y = -Vitesse_balle_Y
                            mur_brique[colone][ligne] = JAUNE
                            brique_compte += point_par_brique
                            break

                        if mur_brique[colone][ligne] == ROUGE:
                            Vitesse_balle_Y = -Vitesse_balle_Y
                            mur_brique[colone][ligne] = ORANGE
                            brique_compte += point_par_brique
                            break
                        
            X_balle += Vitesse_balle_X
            Y_balle += Vitesse_balle_Y

### AFFICHAGE
        
    # FOND
    fenetre.fill(BLEU_FONCE)
    pygame.key.set_repeat(300, 5)

    if jeu_selection_debut:

        ##mise à jour
        #scores
        texte_str_score = "POINTS : " + str(brique_compte)
        texte_score = police.render(texte_str_score,1,NOIR)

        #vie
        texte_str_vie_restante = "VIE : " + str(vie)
        texte_vie_restante = police.render(texte_str_vie_restante,1,NOIR)

        #affichage des boutons
        draw.rect(fenetre, debut_couleur, brique_debut_parametre)
        draw.rect(fenetre, stop_couleur, brique_stop_parametre)
        draw.rect(fenetre, score_couleur, brique_score_parametre)
        draw.rect(fenetre, vie_restante_couleur, brique_vie_restante_parametre)

        #affichage du textes
        fenetre.blit(texte_debut, texte_debut_position)
        fenetre.blit(texte_stop, texte_stop_position)
        fenetre.blit(texte_info, texte_info_position)
        fenetre.blit(texte_score, texte_score_position)
        fenetre.blit(texte_vie_restante, texte_vie_restante_position)

    if mort:

        ##mise à jour
        #scores
        texte_str_score = "POINTS : " + str(brique_compte)
        texte_score = police.render(texte_str_score,1,NOIR)

        #vie
        texte_str_vie_restante = "VIE : " + str(vie)
        texte_vie_restante = police.render(texte_str_vie_restante,1,NOIR)

        draw.rect(fenetre, encore_couleur, brique_encore_parametre)
        draw.rect(fenetre, stop_couleur, brique_stop_parametre)
        draw.rect(fenetre, score_couleur, brique_score_parametre)
        draw.rect(fenetre, vie_restante_couleur, brique_vie_restante_parametre)

        fenetre.blit(texte_encore, texte_encore_position)
        fenetre.blit(texte_stop, texte_stop_position)
        fenetre.blit(texte_info, texte_info_position)
        fenetre.blit(texte_score, texte_score_position)
        fenetre.blit(texte_vie_restante, texte_vie_restante_position)
        fenetre.blit(texte_perdu, texte_perdu_position)

    if gagner:

        ##mise à jour
        #scores
        texte_str_score = "POINTS : " + str(brique_compte)
        texte_score = police.render(texte_str_score,1,NOIR)

        #vie
        texte_str_vie_restante = "VIE : " + str(vie)
        texte_vie_restante = police.render(texte_str_vie_restante,1,NOIR)

        draw.rect(fenetre, encore_couleur, brique_encore_parametre)
        draw.rect(fenetre, stop_couleur, brique_stop_parametre)
        draw.rect(fenetre, score_couleur, brique_score_parametre)
        draw.rect(fenetre, vie_restante_couleur, brique_vie_restante_parametre)

        fenetre.blit(texte_encore, texte_encore_position)
        fenetre.blit(texte_stop, texte_stop_position)
        fenetre.blit(texte_info, texte_info_position)
        fenetre.blit(texte_score, texte_score_position)
        fenetre.blit(texte_vie_restante, texte_vie_restante_position)
        fenetre.blit(texte_gagner, texte_gagner_position)
    
    if jeu_lancer :
            
        ##mise à jour
        #scores texte
        texte_str_score = "POINTS : " + str(brique_compte)
        texte_score = police.render(texte_str_score,1,NOIR)

        #vie text
        texte_str_vie_restante = "VIE : " + str(vie)
        texte_vie_restante = police.render(texte_str_vie_restante,1,NOIR)

        #bouton vie et scores
        draw.rect(fenetre, score_couleur, brique_score_parametre)
        draw.rect(fenetre, vie_restante_couleur, brique_vie_restante_parametre)
        
        #valeurs vie et scores
        fenetre.blit(texte_score, texte_score_position)
        fenetre.blit(texte_vie_restante, texte_vie_restante_position)
        
        # RAQUETTE
        draw.line(fenetre, GRIS, (X_debut, Y_raquette), (X_fin, Y_raquette), epaiseur_raquette)

        ##BRIQUE LIGNE 1
        draw.rect(fenetre,mur_brique[0][0],(X_brique_1, Y_brique_1 , largeur_brique, longeur_brique))
        draw.rect(fenetre,mur_brique[0][1],(X_brique_2, Y_brique_1 , largeur_brique, longeur_brique))
        draw.rect(fenetre,mur_brique[0][2],(X_brique_3, Y_brique_1 , largeur_brique, longeur_brique))
        draw.rect(fenetre,mur_brique[0][3],(X_brique_4, Y_brique_1 , largeur_brique, longeur_brique))
        draw.rect(fenetre,mur_brique[0][4],(X_brique_5, Y_brique_1 , largeur_brique, longeur_brique))

        ##BRIQUE LIGNE 2
        draw.rect(fenetre,mur_brique[1][0],(X_brique_1, Y_brique_2 , largeur_brique, longeur_brique))
        draw.rect(fenetre,mur_brique[1][1],(X_brique_2, Y_brique_2 , largeur_brique, longeur_brique))
        draw.rect(fenetre,mur_brique[1][2],(X_brique_3, Y_brique_2 , largeur_brique, longeur_brique))
        draw.rect(fenetre,mur_brique[1][3],(X_brique_4, Y_brique_2 , largeur_brique, longeur_brique))
        draw.rect(fenetre,mur_brique[1][4],(X_brique_5, Y_brique_2 , largeur_brique, longeur_brique))

        ##BRIQUE LIGNE 3
        draw.rect(fenetre,mur_brique[2][0],(X_brique_1, Y_brique_3 , largeur_brique, longeur_brique))
        draw.rect(fenetre,mur_brique[2][1],(X_brique_2, Y_brique_3 , largeur_brique, longeur_brique))
        draw.rect(fenetre,mur_brique[2][2],(X_brique_3, Y_brique_3 , largeur_brique, longeur_brique))
        draw.rect(fenetre,mur_brique[2][3],(X_brique_4, Y_brique_3 , largeur_brique, longeur_brique))
        draw.rect(fenetre,mur_brique[2][4],(X_brique_5, Y_brique_3 , largeur_brique, longeur_brique))

        #BALLE
        pygame.draw.ellipse(fenetre, GRIS, (X_balle, Y_balle, diamete_balle, diamete_balle))

    # Rafraichissement
    pygame.display.flip()

pygame.quit()