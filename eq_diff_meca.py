from scipy.integrate import odeint
from pylab import *

def F(liste_f,t,alpha,g):
    x=liste_f[0]
    x_p=liste_f[1]
    y=liste_f[2]
    y_p=liste_f[3]
    x_pp= -alpha*sqrt(x_p**2+y_p**2) *x_p
    y_pp = -alpha*sqrt(x_p**2+y_p**2) *y_p -g
    return [x_p,x_pp,y_p,y_pp]

liste_t= linspace(0,5,100)
for theta in linspace(0,pi/2,15):
    results=odeint(F,[0,10*cos(theta),0,10*sin(theta)],liste_t,(0.5,9.8))
    plot(results[:,0],results[:,2])
show()
