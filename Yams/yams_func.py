"""
    Author : GOESSEL Guillaume (g_goessel@outlook.com)

    Ceci est le fichier ou sont stockée mes fonctions
"""

import random

def demande(var_type_ref, phrase):
    """
        Cette fonction permet de demande à l'utilisateur de rentrer une
        variable du type var_type_ref avec comme question phrase.
    """
    while 1:
        input_var = input(phrase)
        #vérifie si l'entrée est correcte
        try:
            if type(var_type_ref) == int:
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



def relance(inter):
    """
        Cette fonction demande le nombre de relances (nbr_relances)
        Le paramètre inter permet de savoir la combinaison initiale
        On retourne la nouvelle combinaison de dés
    """
    deja_rejoues = []

    while 1:
        nbr_relances = demande(0, 'Combien de dés voulez vous relancer ?')
        if nbr_relances>=0 and nbr_relances<=5:
            break
        else:
            print('\nImpossible de relancer plus de 5 dés.')

    for i in range(nbr_relances):
        while 1:
            k = demande(0, 'Quel dé voulez vous relancer ?\n')
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
    return inter
