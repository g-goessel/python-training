# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:06:31 2013

@author: eleve
"""

from pylab import matplotlib, plot, show
from random import randint
#from multiprocessing import *
import time
import timeit


liste_x=[]
liste_y=[]
time_origin=time.clock()
nbr_repetitions=4

def brown(p):
    y=0
    for k in range(p):
       a=randint(0,2)
       if a==1:
           y+=1
       else:
           y-=1
    return y

def Thread():
  for i in range(100000):
    a=brown(50)
    if a in liste_x:
      liste_y[liste_x.index(a)]+=1
    else:
      liste_x.append(a)
      liste_y.append(1)

Thread()

time_end=time.clock()
print(time_end - time_origin)
plot(liste_x, liste_y,'bo')
show()
