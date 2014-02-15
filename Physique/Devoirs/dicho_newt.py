from scipy import misc

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
        print(a,b,c,ite)
            
    return (a,b,ite)
    
    
def newton(F,a,epsilon,DFDT='none'):
    ite=0
    if DFDT=='none':
        DFDT=misc.derivative(F,a,10**(-5))
        
    while abs(F(a))>epsilon:
        #On verifie si on a trouvé une racine
        if abs(F(a))<=epsilon: return(a)
        #sinon on fait une boucle supplémentaire
        ite+=1
        a = -F(a)/DFDT +a
        DFDT=misc.derivative(F,a,10**(-5))
        
    return (a,ite)
        

def secante(F,a,b,epsilon):
    ite=0

    while abs(F(a))>epsilon:
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
        a=b - F(b)*(b-c)/(F(b)-F(c))
    return(a,ite)

def func(x):
    return (x-123)**2-8
    
print(dichotomie(func,120,134.30,10**(-5)))
print(newton(func,1120,10**(-5)))
print(secante(func,1120,1234.30,10**(-5)))
    
