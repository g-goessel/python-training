# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:21:34 2013

@author: eleve
"""

from pylab import *
import numpy
from scipy.integrate import odeint


def F(liste, t, q, omega, E):
    return [liste[1], -(omega / q) * liste[1] - omega * liste[0] + omega ** 2 * E]

liste_t = linspace(0, 20, 10000)
for i in linspace(0.1, 5, 10):
    liste_sol = odeint(F, [0, 0], liste_t, (i, 2, 10))
    liste_y = liste_sol[:, 0]
    liste_y_one = liste_sol[:, 1]
    subplot(i + 1, 2, 1)
    plot(liste_t, liste_y)
    plot(liste_t, liste_y_one)
    subplot(i + 1, 2, 2)
    plot(liste_y_one, liste_y)

show()
