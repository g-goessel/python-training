from scipy import misc
from numpy import arctan, sqrt,exp, cos,pi,log

#cela permet aux divisions par zero de lever une exception en faisant réagir le try aux "RuntimeWarning"
import warnings
warnings.filterwarnings('error')


def dichotomie(F,a,b,epsilon):
    ite=0
    if F(a)<F(b): 
        sign=1
    else: 
        sign =-1
        
    while abs(a-b)>epsilon:
        ite+=1
        c=(a+b)/2
        if F(c)==0: return (c,ite)
        elif sign*F(c)>0:
            b=c
        else: 
            a=c
            
    return ((a+b)/2,ite)
    
    
def newton(F,a,epsilon,DFDT='none'):
    ite=0
    if DFDT=='none':
        DFDT=misc.derivative(F,a,10**(-5))
        
    while abs(F(a))>epsilon:
        try:
            #On verifie si on a trouvé une racine
            if abs(F(a))<=epsilon: return(a)
            #sinon on fait une boucle supplémentaire
            ite+=1
            a = -F(a)/DFDT +a
            DFDT=misc.derivative(F,a,10**(-5))
            #On vérifie que l'algorithme ne diverge pas
            assert a<epsilon*10**25
            assert ite<10**5
        except : 
            return('Divergence de l\'algorithme')
            break
        
    return (a,ite)
        

def secante(F,a,b,epsilon):
    ite=0
    while abs(F(a))>epsilon:
        try:
            #On verifie si on a trouvé une racine
            if F(a)==0 : return(a,ite)
            elif F(b)==0 : return(b,ite)
            
            #sinon on fait une boucle supplémentaire

            #ici a = x_{n+1}
            #     b = x_n
            #     c = x_{n-1}
            ite+=1
            c = b
            b = a
            a = b - F(b)*(b-c)/(F(b)-F(c))
            #On vérifie que l'algorithme ne diverge pas 
            assert (a-b)<epsilon*10**25
            assert ite<10**5
        except :
            return('Divergence de l\'algorithme')
            break

    return(a,ite)

def func(x):
    return log(abs(x))
    
print('dichotomie :',dichotomie(func,0.1,10,10**(-5)))
print('newton :',newton(func,0.1,10**(-5)))
print('secante :',secante(func,-2,0.2,10**(-5)))
    
"""
2)Pour la fonction arctan misc.derivative renvoi une valeur arrondie à 0 à la 4ème itération pour une valeure initiale de 10
  La méthode de la sécante diverge également mais moins rapidement.

"""