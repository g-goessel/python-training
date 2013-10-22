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


#premiere demande de relance
nbr_relances = demande('int', 'combien de dés veux tu relancer ?')
relance(nbr_relances, alea)


#deuxieme demande de relance si on n'a pas refusé la remière
if nbr_relances != 0:
    print('\nPremière relance effectuée !')
    print('Vos dés sont maintenant :')
    print(alea,'\n')

    nbr_relances = demande('int', 'combien de dés veux tu relancer ?')
    relance(nbr_relances, alea)
    print('Relances terminées !')
    print('\nVos dés sont maintenant :')
    print(alea)
