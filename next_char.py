# -*- coding: utf-8 -*-


lettres=['abcdefghijklmnopqrstuvwxyz']
e=['é','è']
entree=input('phrase ? \n').lower()
sortie_list=[]
sortie_str=''
for i in range (len(entree)):
    if entree[i] in lettres:
        sortie_list.append(entree[i])
    elif entree[i] in e:
        sortie_list.append('F')
    else:
        sortie_list.append(entree[i])
for i in sortie_list:
    sortie_str+=i
print(sortie_str)
