#le prog n'atteint jamais la fin du while : a executer dans terminal
import math
def f(x):
    return math.exp(x)-x-5
a=1.0
b=5
tour=0
while (f(a)<0 and f(b)>0) and tour<100:
    if f((a+b)/2.0)>0:
        b=(a+b)/2.0
    else:
        a=(a+b)/2.0
    print('nous sommes au tour', tour)
    print('a vaut',a)
    print('b vaut',b)
    print('f(a)=',f(a))
    tour+=1
print(a)
print(b)
