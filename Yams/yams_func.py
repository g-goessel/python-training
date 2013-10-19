"""
    Author : GOESSEL Guillaume (g_goessel@outlook.com)

    Ceci est le fichier ou sont stockée mes fonctions
"""

import random

def demande(type_ref, phrase):
    """
        Cette fonction permet de demande à l'utilisateur de rentrer une
        variable du type de "type_ref" avec comme question "phrase"
    """
    while 1:
        input_var = input(phrase)
        #je vérifie si l'entrée est correcte
        try:
            if type_ref == 'int':
                return int(input_var)
            elif type_ref == 'str':
                return str(input_var)
            elif type_ref == 'float':
                return float(input_var)
        except:
            print('erreur de donnée, recommence')
            continue

        if type(phrase) == type(type_ref):
            break



def relance(nbr, inter):
    """
        Cette fonction exécute le nombre demandé de relances (nbr)
        Le paramètre inter permet de savoir la combinaison initiale
        On retourne la nouvelle combinaison de dés
    """
    deja_rejoues = []
    for i in range(nbr):
        while 1:
            k = demande('int', 'Quel dé veux tu relancer ?\n')
            if k in deja_rejoues:
                print('tu ne peux pas relancer ce dé plusieurs fois !')
            elif type(k) is int and k<=5 and k>0:
                print('dé ', k, ' rejoué')
                deja_rejoues.append(k)
                break
            else:
                print('il est impossible de rejouer ce dé car il n\'existe pas !')
        #on prend l'objet k-1 pour avoir un indice plus naturel
        inter[k-1] = random.randint(1, 6)
    return inter
