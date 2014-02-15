from scipy import *

def dichotomie(F,a,b,epsilon):
    ite=0
    if F(a)>F(b): 
        sign=-1
    else: 
        sign =1
        
    while abs(b-a) >epsilon:
        ite+=1
        c=(a+b)/2
        if sign*F(c)>0:
            b=c
        else: 
            a=c

        print(a,b,c,ite)
            
    return (a,b,ite)
    
    
def newton(F,a,epsilon,DFDT='none'):
    ite=0
    if DFDT=='none':
        DFDT=misc.derivative(F,a,10**(-5))
        
    while abs(F(a))>epsilon:
        #On verifie si on a trouvé une racine
        if F(a)==0: break
        #sinon on fait une boucle supplémentaire
        ite+=1
        a = -F(a)/DFDT +a
        DFDT=misc.derivative(F,a,10**(-5))
        
    return (a,ite)
        

        
        

def func(x):
    return -x+3
    
print(dichotomie(func,-30,12.30,10**(-2)))
    
