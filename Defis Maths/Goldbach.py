from random import randint
from math import sqrt, log, floor
from lib.pynma import pynma
from multiprocessing import Pool
import time
import gmpy2
#see here for gmpy2 : http://code.google.com/p/gmpy/

# 50x on calcul 10000 termes en meme temps
# je ne dépasse pas 10000 pour ne pas saturer la mémoire
etape = 10**6

#nombre de fois où je calcul les "etape" termes
#ainsi on calcul au total repet*etape termes
repet = 50

#n représente le nombre de départ à partir on commence à calculer
n = 10**18

#API perso pour l'envoi de notifs à mon tel
p = pynma.PyNMA( "a7dec75df0f46a2525c378538ed931decaeab3fba94ec22c")

def goldbach(n):
    """teste la conjecture de Golbach en tentant de décomposer n pair (>2) en 2 nb premiers"""

    # verification
    if n<4 or n%2!=0:
        raise(ValueError) ("Erreur: n doit être un nombre entier pair > 2")

    # traitement du cas x=2 qui ne marche que pour n=4
    if n==4:
        return [2,2]

    # autres cas
    x = 3
    while True:

        # calcul de y et test de primalité
        y = n-x
        if gmpy2.is_prime(y,30):
            #print(n,[x,y]) # on a trouvé!
            return (n,[x,y])

        # vérif qu'on a encore la possibilité de trouver une solution
        if x>y:
            return [] # echec!

        # On prend le nombre premier suivant x
        x = gmpy2.next_prime(x)

if __name__ == '__main__':
    pool=Pool(None)
    a=time.clock()
    for k in range(repet):
        result = pool.map(goldbach, [i for i in range(n,n+etape,2)])
        for l in range(len(result)):
            print(result[l])
        n+=10**5
        p.push("Golbach","Nouvelle étape atteinte !", "10^38 + "+str(k)+"10^6")

    b=time.clock()
    print('took ',b-a)
