"""
This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

Code disponible ici : bit.ly/1eHdCbY 
"""


from pylab import *
import numpy as np
from scipy.integrate import odeint
import scipy.optimize as opt

#champ de gravitation
g=9.8
#distance epaule/centre de gravité du tronc
h=0.7
#longeur d'un bras
b=1
#hauteur des pieds aux épaules
c=1.7
#masse d'un bras
m=5
#masse du corps privés des deux bras
M=65

#valeurs initiales
theta_zero=pi/7
dtheta_zero=0
d2theta_zero=0
alpha1_zero=pi/2
alpha2_zero=pi/2

def OG(theta,alpha1,alpha2):
    return sqrt((c+(-M*h-m*b*(cos(alpha1)+cos(alpha2)))/(M+2*m))**2+(1/(M+2*m)*(sin(alpha2)-sin(alpha1)))**2)

def cal(x,theta):
    #merci http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html
    #On veut que la dérivée seconde soit négative
    #ici x[0]=alpha1
    #x[1]=alpha2
    f= [c*sin(theta)+(m*b*(cos(theta)*(sin(x[1])-sin(x[0]))-sin(theta)*(cos(x[0])+cos(x[1])))-M*h*sin(theta))/(M+2*m)-10**(-5),0]
    return f


def F(liste,t,alpha1,alpha2):
    theta=liste[0]
    dthetadt=liste[1]
    (alpha1,alpha2)=opt.root(cal,x0=(0,0),jac=False,args=(theta)).x
    return (dthetadt,-g/(OG(theta,alpha1,alpha2)**2)*(c*sin(theta)+(m*b*(cos(theta)*(sin(alpha2)-sin(alpha1))-sin(theta)*(cos(alpha1)+cos(alpha2)))-M*h*sin(theta))/(M+2*m)))


liste_t=linspace(0,1,100)
solution=odeint(F,[theta_zero,dtheta_zero,d2theta_zero],liste_t,(alpha1_zero,alpha2_zero))

#on nettoie solution car un des algo (odeint probablement) diverge et sort nimporte quoi
solution2=list()
try:
    for i in solution:
        if i[0] >10**(-15) and i[0] <100:
            solution2.append(i[0])
        else: assert()
except: pass

liste_t_2=list()
for i in range(len(solution2)):
    liste_t_2.append(liste_t[i])
plot(liste_t_2,solution2)
show()
