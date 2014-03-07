# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 11:15:01 2014

@author: eleve
"""

from pylab import *

def resol(M,E):
    n=len(M)
    try:
        for k in range(n):
            i=0
            while 1:
                pivot = M[k+i,k] 
                print(pivot)
                if pivot !=0:
                    if i !=0:
                        M_2=M.copy()
                        nvelle_ki=M[k]
                        nvelle_k=M[k+i]
                        M_2[k]=nvelle[k]
                        M_2[k+i]=nvelle_ki
                        M=M_2
                    print(M)
                    break
                elif i >n+1:
                    #assert()
                    pass
                else:
                    i+=1
                print(M)
                
            for i,j in range(k+1,n+1),range(k,n+1):
                q_i=M[i,k]/M[k,k]
                M[i,j]-=q_i*M[k,j]
                print(M)
    except :
            print("pivot nul")
        
M=array([[1,3,4],[2,7,-2],[0,1,5]])
E=array([[4,7,9]])

print(resol(M,E))
