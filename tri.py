# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 12:35:58 2013

@author: eleve
"""
from pylab import randint
from time import time

def genere_liste(n):
    liste=[]
    for i in range(n):
        liste.append(randint(1,10*n))
    return liste

def decoupe(liste_1):
    n=0
    resultat=[]
    for i in liste_1:
        try:
            #on essaie de decouper la liste_1 en ensembles de deux elements
            resultat.append([liste_1[n],liste_1[n+1]])
            n+=2
        except:
            #Si cela echoue c'est qu'il ne reste plus qu'un élément
            if len(liste_1)%2:
                resultat.append(([liste_1[n]]))
            break
    return resultat

def tri(liste_1, liste_2):
    sortie=[]
    while len(liste_1)>0 or len(liste_2)>0:
        try:
            if liste_1[0]<liste_2[0]:
                sortie.append(liste_1.pop(0))
            else :
                sortie.append(liste_2.pop(0))
        except:
            if len(liste_1)==0:
                sortie+=liste_2
            elif len(liste_2)==0:
                sortie+=liste_1
            break
    return sortie


intermediaire=[]

liste_gen=genere_liste(42)
try:
    for i in range(len(liste_gen)//2 +1):
        intermediaire=tri(liste_gen[i],liste_gen[i+1])
except:
    pass
print(intermediaire)
print(tri([0,1], [5,8]))
