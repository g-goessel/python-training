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

def moyenne(a):
    somme=0
    for i in a:
        somme+=i
    return somme/len(a)
    
def decoupe(liste_1):
    length=len(liste_1)//2
    liste_2=[]
    for i in range(length):
        liste_2.append(liste_1.pop(0))
    return[liste_1, liste_2]
    
def tri(liste_a_trier):
    if lenliste_a_trier
            
print(decoupe(genere_liste(50)))
