from random import randint
from math import sqrt, log, floor
from multiprocessing import Pool
import sys
import time
import gmpy2
#see here for gmpy2 : http://code.google.com/p/gmpy/

#bibliotheques perso, a supprimer :
from lib.pyPushBullet.pushbullet import PushBullet
from lib import personal_keys

#API perso pour l'envoi de notifs à mon tel
p = PushBullet(personal_keys.perso("API_PB"))

# Désigne le nombre de calculs à effectuer en meme temps
# Ne pas dépasser 10**6 pour 3Go de RAM libre
etape = 10**4

# Nombres d'étapes nécessaires avant de recevoir un message d'etat du calcul
step_msg=10**1

#Adresse du fichier où sont stockés les résultats
out_dir='/mnt/sdc1/Goldbach.txt'
#On enlève ce qu'il y avait dedans
open(out_dir,'w').close()



def goldbach(n):
    """teste la conjecture de Golbach en tentant de décomposer n pair (>2) en 2 nb premiers"""

    x = 3
    while True:
        # calcul de y et test de primalité
        y = n-x
        if gmpy2.is_prime(y,20):
            return (n,[int(x),int(y)])

        # On prend le nombre premier suivant
        x = gmpy2.next_prime(x)

if __name__ == '__main__':
    a=time.clock()
    n=4*10**14
    nbr_boucle=0
    with Pool(None) as pool:
        while 1:
            nbr_boucle+=1
            #On va changer la sortie du terminal pour la rédiriger directement dans in fichier
            #On sauvegarde l'état précedent pour pouvoir le restaurer par la suite
            stdout_old=sys.stdout
            sys.stdout = open(out_dir,'a')
            a=time.process_time()
            for i in range(step_msg):
                result = pool.map(goldbach, [i for i in range(n,n+etape,2)])
                print(*result,sep='\n')
                n+=etape
            b=time.process_time()
            p.pushNote(personal_keys.perso("PB_Nexus5"),"Golbach", str(nbr_boucle)+'*10^'+str(int(log(step_msg*etape)/log(10))+1))
            sys.stdout.close()
            # On restaure stdout pour retrouver une sortie terminal
            sys.stdout=stdout_old
            print('Etape actuelle :', n)
            print('Temps nécessaire : ',int((b-a)*10))

