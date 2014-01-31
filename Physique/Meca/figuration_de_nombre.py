# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:44:25 2014

@author: eleve
"""
import math
from pylab import *
import tkinter as tk
import os
from PIL import Image,ImageTk

x=0
y=0
theta=0
a=5
b=3
r=(1+sqrt(5))/2
x_list=list()
y_list=list()
xscale=900
yscale=700

for n in range(int(1*10**6)):
    x_list.append(x)
    y_list.append(y)
    if math.floor(r*(a*n+b))%2 ==0 :
        theta += pi/3
    else :
        theta += -2*pi/3
    x+=cos(theta)
    y+=sin(theta)

plot(x_list,y_list,',')
try :
    os.mkdir('temp')
except:
    pass
fen=tk.Tk()
savefig('temp/sauvegarde.png')
close()
image =Image.open('temp/sauvegarde.png')
largeur_image_i=image.size[0]
hauteur_image_i=image.size[1]
ratio=min([xscale/largeur_image_i,yscale/hauteur_image_i])
largeur = int(largeur_image_i*ratio)
hauteur = int(hauteur_image_i*ratio)
imagebis=image.resize((largeur,hauteur),Image.BILINEAR)
imagebis.save('temp/affichage.png')
photo = ImageTk.PhotoImage(imagebis)
figure=tk.Canvas(fen,width=xscale,height=yscale)
figure.grid(row=1,column=1,rowspan=4)
item=figure.create_image(0,0,anchor=tk.NW,image=photo)
tk.mainloop()
    
