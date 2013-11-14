# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:40:03 2013

@author: eleve
"""

def suite(n):
	u=1
	for i in range(2,n+1):
		u=u**2-4*i
	return u

print(suite(int(input('n='))))

