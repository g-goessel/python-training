import numpy

nbLignes = int(input("nbLignes \n"))
nbColonnes = int(input("nbColonnes \n"))
tableau = list()
for i in range(nbLignes):
    a = input()
    tableau.append(a.split())

for i in tableau:
    if "0" in i:
        result=1
        break
    else:
        result =0

def right_test(ligne, colonne):
    return tableau[ligne[colonne + 1]]

def down_test(ligne, colonne):
    return tableau[ligne[colonne]+1]

for l in range(tableau):
    for i in range(nbLignes):
        if right_test(l,i)==0 and down_test(l,i)==0:



print(tableau)
