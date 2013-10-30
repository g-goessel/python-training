# -*- coding: utf-8 -*-
"""
    Author : GOESSEL Guillaume (g_goessel@outlook.com)
"""

# jeu du yams
from yams_func import *

#liste contenant les nombres aléatoires des 5 dés
alea = []

for i in range(5):
    alea.append(random.randint(1, 6))
print(alea)


#premiere  relance
#on appel alea_rel1 la liste contenant la valeur des dés après la première relance

alea_rel1=relance(alea)

#deuxieme  relance si la première n'a pas été refusée
if alea != alea_rel1:
    alea=relance(alea_rel1)
else:
    alea=alea_rel1
    print('Relances terminées !')
    print('\nVos dés sont maintenant :')
    print(alea)


#calcul des points
print('Nous allons maintenant calculer vos points')
while 1:
    methode_compt=demande(' ','Voulez vous prendre un numéro ou une figure ? (n/f)')
    #dans le cas ou le joueur veut compter suivant les numéros
    if methode_compt=='n':
        while 1:
            nbr=demande(0,'Quel numéro voulez vous choisir ?')
            if nbr>=1 and nbr <=6:
                points=alea.count(nbr)
                break
            else:
                print('Les valeurs possibles d\'un dés sont comprises entre 1 et 6')
            break
    #dans le cas ou le joueur veut compter suivant une figure
    elif methode_compt=='f':
        while 1:
            fig=demande(0,'Quelle figure voulez vous prendre ?')
        break
    else :
        print('Erreur de donnée, recommencez')
print('Vous avez', points,'points')