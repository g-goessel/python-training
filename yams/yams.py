# -*- coding: utf-8 -*-
"""
    Author : GOESSEL Guillaume (g_goessel@outlook.com)
"""

# jeu du yams
from yams_func import *

#dictionnaire contenant l'ensemble des points
l_scores={}

#liste des combinaisons possibles restantes
combi_dispo=['1','2','3','4','5','6','brelan','full','carre','yams','min','max','suite']

#on a 13 essais
for num_essaie in range(12):

    #liste contenant les nombres aléatoires des 5 dés
    alea = []

    for i in range(5):
        alea.append(random.randint(1, 6))
    print('Vos dés sont :', alea)


    #On effectue les relances
    alea=jette_des(alea)
    print('Relances terminées !')
    #print('\nVos dés sont maintenant :', alea)


    #calcul des points
    print('Nous allons maintenant calculer vos points')
    while 1:
        print('Combinaisons disponibles :', combi_dispo)
        methode_compt=demande(' ','Quelle combinaison voulez vous jouer ? ')
        
        if methode_compt in combi_dispo:
            combi_dispo.remove(methode_compt)
            break
        else:
            print('Erreur : combinaison non reconnue')
    
    try:
        #On regarde si l'utilisateur à choisit une combinaison de chiffres
        chiffre=int(methode_compt)
        l_scores[methode_compt]=score(alea)[0][chiffre-1]

    except:
        #Sinon il s'agit d'une autre combinaison
        if methode_compt=='brelan':
            l_scores[methode_compt]=score(alea)[1]
        elif methode_compt=='full':
            l_scores[methode_compt]=score(alea)[2]
        elif methode_compt=='carre':
            l_scores[methode_compt]=score(alea)[3]
        elif methode_compt=='yams':
            l_scores[methode_compt]=score(alea)[4]
        elif methode_compt=='suite':
            l_scores[methode_compt]=score(alea)[5]
        elif methode_compt=='min':
            l_scores[methode_compt]=score(alea)[6]
        elif methode_compt=='max':
            l_scores[methode_compt]=score(alea)[7]


    print('\nRésumé des scores',l_scores,'\n')
