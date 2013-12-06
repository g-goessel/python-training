# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:35:26 2013

@author: eleve
"""
from pylab import *
import numpy
import math

def intt(f,a,b,n):
    liste=linspace(a,b,n+1)
    integrale=0
    plot(liste,f(liste))
    for i in range(len(liste)-1):
        integrale+=(f(liste[i])+f(liste[i+1]))*(liste[i+1]-liste[i])/2
        fill_between(liste,f(liste[i]),f(liste[i+1]))
    return integrale


def f(x):
    return x**2
    
print(intt(f,0,1,1000))
show()
