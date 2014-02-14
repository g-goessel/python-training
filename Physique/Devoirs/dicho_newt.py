from scipy import misc

def dichotomie(F,a,b,epsilon):
    ite=0
    if F(a)>F(b): 
        sign=-1
    else: 
        sign =1
        
    while abs(b-a) >epsilon:
        c=(a-b)/2
        if sign*F(c)>0:
            a=c
        else: 
            b=c
            
    return (a,b,ite)
    
    
def newton(F,a,epsilon,DFDT=0):
    ite=0
    if DFDT==0:
        DFDT=misc.derivative(F,a,10**(-5))
        
    while F(a)>epsilon and epsilon>F(a):
        ite+=1
        a = +F(a)/DFDT +a
        DFDT=misc.derivative(F,a,10**(-5))
        
    return a,ite
        

        
        

def func(x):
    return x**2
    
print(newton(func,-3,0.1))
    
