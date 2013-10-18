# fichier de fonctions

import random

#demande permet d'obtenir une variable du meme type que ref
def demande(type_ref,phrase):
    while 1:
        input_var=input(phrase)
        #je vérifie si l'entrée est correcte
        try:
            if type_ref=='int':
                return int(input_var)
            elif type_ref=='str':
                return str(input_var)
            elif type_ref=='float':
                return float(input_var)
        except:
            print('erreur de donnée, recommence')
            continue

        if type(nbr_relances_1)==type(ref):
            break



def relance(nbr,inter):
    #on effectue les relances souhaitées
    deja_rejoues=[]
    for i in range(nbr):
        while 1:
            k=demande('int','Quel dé veux tu relancer ?\n')
            if k in deja_rejoues:
                print('tu ne peux pas relancer ce dé plusieurs fois !')
            elif type(k) is int and k<=5 and k>0:
                print('dé ',k,' rejoué')
                deja_rejoues.append(k)
                break
            else:
                print('il est impossible de rejouer ce dé car il n\'existe pas !')
        #on prend l'objet k-1 pour avoir une lecture naturelle de l'indice du dé
        inter[k-1]=random.randint(1, 6)
    return inter
