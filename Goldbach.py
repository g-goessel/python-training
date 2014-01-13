from random import randint
from math import sqrt, log, floor
from lib.pynma import pynma
import time
import gmpy2

p = pynma.PyNMA( "a7dec75df0f46a2525c378538ed931decaeab3fba94ec22c")

def estpremier(n):
    """Dit si le nombre entier n est premier ou non (méthode par division)"""

    # traitement du cas: si n est pair
    if n%2==0:
        # ici, n est pair: il n'est premier que si c'est 2
        if n==2:
            return True
        return False

    # traitement des autres cas: n est impair
    xmax = int(sqrt(n))+1
    x = 3
    while x<xmax:
        if n%x==0:
            return False # x est un diviseur de n: n n'est donc pas premier
        x += 2

    # ici, on n'a trouvé aucun diviseur de n avant xmax: n est premier
    return True

def goldbach(n):
    """teste la conjecture de Golbach en tentant de décomposer n pair (>2) en 2 nb premiers"""

    # verification
    # if n<4 or n%2!=0:
    # raise(ValueError) ("Erreur: n doit être un nombre entier pair > 2")

    # traitement du cas x=2 qui ne marche que pour n=4
    # if n==4:
    # return [2,2]

    # autres cas
    x = 3
    while True:

        # calcul de y et test de primalité
        y = n-x
        if gmpy2.is_prime(y,1000):
            return [x,y] # on a trouvé!

        # vérif qu'on a encore la possibilité de trouver une solution
        if x>y:
            return [] # echec!

        # recherche du 1er nb premier suivant x
        x += 2
        while not gmpy2.is_prime(x):
            x += 2
n = 4*10**18+2
while 1:
    pass
    a=time.clock()
    r = goldbach(n)
    print(n, r)
    b=time.clock()
    print(b-a)
    #p.push("Golbach",str(e), str(r[0]))
    if len(r) == 0:
        print("échec")
    n+=2
    break
