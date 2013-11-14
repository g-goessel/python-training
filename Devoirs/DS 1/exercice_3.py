# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:06:31 2013

@author: eleve
"""

from pylab import *
from random import randint

liste_x=[]
liste_y=[]

def brown(p):
    y=0
    for i in range(p):
       a=randint(0,2)
       if a==1:
           y+=1
       else:
           y-=1
    return y

for i in range(100000):
    a=brown(50)
    if a in liste_x:
        liste_y[liste_x.index(a)]+=1
    else:
        liste_x.append(a)
        liste_y.append(1)

plot(liste_x, liste_y,'bo')
show()
