# -*- coding: utf-8 -*-

# je déclare les variables
sortie=''

lettres_min='abcdefghijklmnopqrstuvwxyz'
lettres_max=lettres_min.upper()
e='éè'
entree=input('phrase ? \n')
for i in entree:
    if lettres_min.find(i)!=-1:
        if lettres_min.find(i)!=25:
            sortie+=lettres_min[lettres_min.find(i) + 1]
        else:
            sortie+=lettres_min[0]
    elif e.find(i)!=-1:
        sortie+='f'
    elif lettres_max.find(i)!=-1:
        if lettres_max.find(i)!=25:
            sortie+=lettres_max[lettres_max.find(i) + 1]
        else:
            sortie+=lettres_max[0]
    else:
        sortie+=i

print(sortie)
