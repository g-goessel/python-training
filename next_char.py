# -*- coding: utf-8 -*-

# je déclare les variables
sortie=''

lettres='abcdefghijklmnopqrstuvwxyz'
e='éè'
entree=input('phrase ? \n').lower()
for i in entree:
    search=lettres.find(i)
    if search!=-1:
        sortie+=lettres[search+1]
    elif e.find(i)!=-1:
        sortie+='f'

print(sortie)
