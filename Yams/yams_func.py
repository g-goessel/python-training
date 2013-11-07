"""
    Author : GOESSEL Guillaume (g_goessel@outlook.com)

    Ceci est le fichier ou sont stockée mes fonctions
"""

import random

def demande(var_type_ref, phrase):
    """
        Cette fonction permet de demande à l'utilisateur de rentrer une
        variable du type de "var_type_ref" avec comme question "phrase".
    """
    while 1:
        input_var = input(phrase)
        #vérifie si l'entrée est correcte
        try:
            if input_var == '':
                #si l'entrée est vide on suppose que l'utilisateur rentre 0
                return 0
            elif type(var_type_ref) == int:
                return int(input_var)
            elif type(var_type_ref) == str:
                return str(input_var)
            elif type(var_type_ref) == float:
                return float(input_var)
        except:
            print('Erreur de donnée, recommencez')
            continue

        # Si la conversion a reussi on sort
        if type(phrase) == type(var_type_ref):
            break



def jette_des(inter):
    """
        Cette fonction demande le nombre de relances ("nbr_relances")
        Le paramètre "inter" permet de savoir la combinaison initiale de dés
        On retourne la nouvelle combinaison de dés
        relance_2 permet d'effectuer deux relances si la première n'est pas refusée
    """
    relance_2=2

    while relance_2>0:
        while 1:
            nbr_relances = demande(0, 'Combien de dés voulez vous relancer ? [0] ')
            if nbr_relances>0 and nbr_relances<=5:
                relance_2-=1
                break
            elif nbr_relances==0:
                relance_2=0
                break
            elif nbr_relances>5:
                print('\nImpossible de relancer plus de 5 dés.')
            else:
                print('Cela n\' a aucun sens !')

        deja_rejoues = []
        for i in range(nbr_relances):
            while 1:
                k = demande(0, 'Quel dé voulez vous relancer ? ')
                if k in deja_rejoues:
                    print('Vous ne pouvez pas relancer ce dé plusieurs fois !')
                elif type(k) is int and k<=5 and k>0:
                    print('dé ', k, ' rejoué')
                    deja_rejoues.append(k)
                    break
                else:
                    print('Il vous est impossible de rejouer ce dé car il n\'existe pas !')
            #on prend l'objet k-1 pour avoir un indice plus naturel
            inter[k-1] = random.randint(1, 6)
        print('Vos dés sont maintenant :', inter)
    return inter

def score(des):
    """
        Cette fonction score retourne la liste des scores possibles
        pour chaque combinaison
        Chaque combinaison possèdera son score inscrit dans une variable
        portant son nom (sauf pour les chiffres où on a une liste)
    """
    chiffres=[]
    for c in range(6):
        chiffres.append(des.count(c+1))

    if 5 in chiffres:
        yams=(chiffres.index(5)+1)*5+50
    else: yams=0

    if 4 in chiffres:
        carre=(chiffres.index(4)+1)*4+30
    else: carre=0

    if 3 in chiffres:
        brelan=(chiffres.index(3)+1)*3+10
        if 2 in chiffres:
            full=sum(des)
        else: full=0
    else:
        brelan=0
        full=0

    if  des[0]==1 and des[1]==2 and des[2]==3 and des[3]==4 and des[4]==5:
        suite=35
    elif des[0]==2 and des[1]==3 and des[2]==4 and des[3]==5 and des[4]==6:
        suite=40
    else: suite=0

    comb_min=-sum(des)
    comb_max=sum(des)

    return [chiffres, brelan, full, carre, yams, suite, comb_min, comb_max]
