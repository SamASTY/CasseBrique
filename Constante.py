import random
import copy

#COULEUR
ROUGE = (145, 38, 14)
JAUNE = (240, 227, 107)
BLEU_FONCE = (80, 178, 201)
ORANGE = (254, 163, 71)
NOIR = (0, 0, 0)
GRIS = (116, 116, 116 )
BLANC = (255, 255, 255)

#GENERATION DES COULEURS ALEATOIRES
def assignation_couleur_brique ():
    mur_brique = [[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
    for ligne in range (len(mur_brique)):
        for brique in range (len(mur_brique[ligne])):
            mur_brique[ligne][brique] = random.choice([ROUGE, ORANGE, JAUNE])
    return mur_brique

#GENERATION D UNE VALEUR APELATOIRE POUR LA DIRECTION DE LA BALLE
def dir_aleatoire():
    valeur = random.choice((-1,1))
    return valeur


#CALCUL DU SCORES MAXIMUM
def score(mur):
    scores_max = 0
    for ligne in range(len(mur)):
        for colone in range(len(mur[ligne])):
            if mur[ligne][colone] == ROUGE :
                scores_max += 300
            if mur[ligne][colone] == ORANGE :
                scores_max += 200
            if mur[ligne][colone] == JAUNE :
                scores_max += 100
    return scores_max

#assignation du mur et sauvegarde
mur_brique = assignation_couleur_brique()
copie_brique = copy.deepcopy(mur_brique)
point_par_brique = 100

#Info du joueur
vie = 3
brique_compte = 0
brique_compte_max = score(mur_brique)

#FENETRE
taille = largeur, longueur = 1000, 1000

###TEXTE
#jouer
texte_debut_position = (300, 600)
#stop
texte_stop_position = (600, 600)
#rejouer
texte_encore_position = (300, 600)
#scores
texte_str_score = "POINTS : " + str(brique_compte)
texte_score_position = (0, 970)
#vie
texte_str_vie_restante = "VIE : " + str(vie)
texte_vie_restante_position = (905, 970)
#information de jeu
texte_info_position = (150, 400)
#Gagner
texte_gagner_position = (450, 500)
#Perdu
texte_perdu_position = (450, 500)


###BOUTON
#taille
largeur_bouton = 200
longueur_bouton = 100

#parametre
brique_debut_parametre = (260, 565 , largeur_bouton, longueur_bouton)
brique_stop_parametre = (560, 565 , largeur_bouton, longueur_bouton)
brique_encore_parametre = (260, 565 , largeur_bouton, longueur_bouton)
brique_score_parametre = (900, 960 , largeur_bouton, longueur_bouton)
brique_vie_restante_parametre = (0, 960 , largeur_bouton + 15 , longueur_bouton)

#couleur
debut_couleur = encore_couleur = stop_couleur = score_couleur = vie_restante_couleur = JAUNE

###RAQUETTE
#coordonnees
X_debut = 425
X_fin = X_debut + 150
Y_raquette = 850

#coordonnées pour le repositionemment de la raquette
X_debut_copy = 425
X_fin_copy = X_debut + 150
Y_raquette_copy = 850

#vitesses
vitesses_raquette = 5

#epaisseur
epaiseur_raquette = 8

###BRIQUE
#Parametre
largeur_brique = 194
longeur_brique = 125

#coordonnee
X_espace = 5
Y_espace = 5

#MUR DE BRIQUE AFFECTATION COORDONNEE
#colonne
X_brique_1 = largeur_brique*0 + X_espace*1
X_brique_2 = largeur_brique*1 + X_espace*2
X_brique_3 = largeur_brique*2 + X_espace*3
X_brique_4 = largeur_brique*3 + X_espace*4
X_brique_5 = largeur_brique*4 + X_espace*5

#ligne
Y_brique_1 = longeur_brique*0 + Y_espace*1
Y_brique_2 = longeur_brique*1 + Y_espace*2
Y_brique_3 = longeur_brique*2 + Y_espace*3


###BALLE
#coordonnee
X_balle = 500
Y_balle = 450

#vitesses
X_sens = dir_aleatoire()
Y_sens = dir_aleatoire()
Vitesse_balle_X = 0.9 * X_sens
Vitesse_balle_Y =0.9 * Y_sens

#taille
diamete_balle = 40

class Selection :
    En_Jeu = 0
    Nouveau_Jeu = 1
    Fin_Jeu = 2

class Nouveau_Debut_Jeu:
    Vie_Init = 3
    X_Debut_Jeu = 425
    Y_Debut_Jeu = 150
    Y_Raquette_Debut = 850
    Vitesse_Raquette_Debut = 5
    X_Balle_Debut = 500
    Y_Balle_Debut = 450
    brique_comptes_init = 0

class LimiteJeu:
    X_Raquette = 0
    Y_Lim_balle = 860


def decrementer(val):
    return val - 1