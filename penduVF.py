# -*- coding: utf8 -*-

# Faire un jeu du pendu.
# "ceci est un jeu du pendu, il y a 6 lettres et tu as 6 chances"
#programme affiche un " _ _ _ _ _ _" et demande "choisit une lettre".
#On répond "a". Si "a" est dans le mot il affiche ou est a et il demande "choisit une nouelle lettre"
#Si a n'est pas dans le mot il dit "perdu, encore 4 chances"
# Si je trouve le bon mot avant d'être mort 'tu as gagné'
# Sinon "GAME OVER".



from random import choice


#FONCTION pour récuperer une lettre
def lettre_recup():
    lettre_select=input("Donne moi une lettre : ")
    lettre_select=lettre_select.lower()
    if len(lettre_select)>1 or not lettre_select.isalpha() :
        print("Vous n'avez pas saisi une lettre valide")
        return lettre_recup()
    
    else:
       return lettre_select


# FONCTION qui affiche les lettres trouvées et qui cache les autres par un "_"
def recup_mot_masque(Lettres_trouvees,mot_secret):
    mot_actuel = ""
    for lettre in mot_secret:
        if lettre in Lettres_trouvees:
            mot_actuel += lettre
        else:
            mot_actuel += " _ "
    return mot_actuel



# on explique le jeu
print("ceci est un jeu du pendu, il y a 6 lettres et tu as 6 chances")


# on defini le mot a trouver aleatoirement dans une liste definie
Liste_mots = ["poivre","ananas", "hoquet","mollet","cinema","avocat","dictee","infini","danser","larves","boulot"]
mot_secret = choice(Liste_mots)

#Cacher le mot secret

mot_cache=''
for lettre in mot_secret:
    lettre=" _ "
    mot_cache=mot_cache+lettre

# on donne la réponse pour faciliter la verification du programme
# a supprimer si "vrai jeu"
print("tu dois trouver le mot suivant :", mot_cache)


# on lance le jeu
Lettres_trouvees = []
Lettres_choisies = []



i=0
while i < 6:

    # saisie d'une lettre
    lettre = lettre_recup()
    if lettre in Lettres_choisies:
        print ("Vous avez déjà séléctionné cette lettre")
        lettre_recup()
    else:
        Lettres_choisies.append(lettre)
    #print(lettres_choisies)

    # verification si dans le mot et affichage
    if lettre in mot_secret:
        Lettres_trouvees.append(lettre)
    mot_trouve = recup_mot_masque(Lettres_trouvees,mot_secret)
    print(mot_trouve)

    # verification si gagne ou perdu
    if mot_trouve == mot_secret:
        print("***************************")
        print("* BRAVO !! Tu as trouvé ! *")
        print("***************************")
        break

    # on compte les essais
    i = i + 1

# si le mot pas trouve apres les essais, alors perdu
if mot_trouve != mot_secret:
    print("***************************")
    print("* PENDU!!! Tu as perdu... *")
    print("***************************")





