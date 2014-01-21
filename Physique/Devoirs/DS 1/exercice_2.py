# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:42:41 2013

@author: eleve
"""
from datetime import date

def nttu():
    while 1:
        a=input('Entrez une date supérieure au 1 janvier 2000 (jj/mm/aaaa)')
        date=a.split('/')
        try:
            if len(date)>3:raise
            for i in range(len(date)):
                date[i]=int(date[i])
            if date[2]>=2000:
                break
            raise
        except:
            print('erreur de donnée')
    return date

day=nttu()

d0 = date(2000, 1,1)
d1 = date(day[2], day[1], day[0])
delta = d1 - d0
print(delta.days)
