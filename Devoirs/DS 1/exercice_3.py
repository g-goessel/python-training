# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:06:31 2013

@author: eleve
"""

from pylab import *
from random import randint
import threading
import time

liste_x=[]
liste_y=[]
time_origin=time.clock()

def brown(p):
    y=0
    for k in range(p):
       a=randint(0,2)
       if a==1:
           y+=1
       else:
           y-=1
    return y

def temp_multi():
  a=brown(50)
  if a in liste_x:
    liste_y[liste_x.index(a)]+=1
  else:
    liste_x.append(a)
    liste_y.append(1)

def Thread_1():
  for i in range(100000):
    a=brown(50)
    if a in liste_x:
      liste_y[liste_x.index(a)]+=1
    else:
      liste_x.append(a)
      liste_y.append(1)

t1 = threading.Thread(target=Thread_1)
t2 = threading.Thread(target=Thread_1)
t3 = threading.Thread(target=Thread_1)
t4 = threading.Thread(target=Thread_1)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

time_end=time.clock()
print(time_end - time_origin)
plot(liste_x, liste_y,'bo')
show()
