# -*- coding: utf-8 -*-
"""
This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

@author: g_goessel
"""
from pylab import randint
from time import time

def genere_liste(n):
    #Generate a random list
    liste=[]
    for i in range(n):
        liste.append(randint(1,10*n))
    return liste

def merge(l_1,l_2):
    out=list()
    while len(l_1)!=0 and len(l_2)!=0:
        if l_1[0]<l_2[0]:
            out.append(l_1.pop(0))
        else:
            out.append(l_2.pop(0))
    #If lists haven't been completely read, we do it
    if len(l_1)!=0:
        out+=l_1
    elif len(l_2)!=0:
        out+=l_2
    return out


def decoupe(l):
    #This function cuts l in small lists of 2 ordered elements
    out=list()
    if len(l)<=1:
        return l
    else:
        for i in range(len(l)//2):
            if l[2*i]<l[2*i+1]:
                out.append([l[2*i],l[2*i+1]])
            else:
                out.append([l[2*i+1],l[2*i]])

        if len(l)%2 != 0:
            out.append([l[len(l)//2 +1]])
        return out

for i in range(5):
    t_start=time()
    #Genrates a list and then cuts it with decoupe
    liste=decoupe(genere_liste(100001))
    #We merge every two lists in liste until they're is only one left
    while len(liste)!=1:
        for i in range(len(liste)//2):
            liste.append(merge(liste[0],liste[1]))
            liste.pop(0)
            liste.pop(0)

    t_end_homemade=time()

    print('\nMine took : ', t_end_homemade - t_start)

    #We do it all over again with a fresh new list
    liste=decoupe(genere_liste(100001))
    liste.sort()
    t_end_builtin=time()

    print('The built-in took : ', t_end_builtin - t_end_homemade)
    print('Ratio : ', (t_end_homemade - t_start)/(t_end_builtin - t_end_homemade))
