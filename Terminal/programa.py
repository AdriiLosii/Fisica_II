import numpy as np
import matplotlib.pyplot as plt
from funciones import *

center=[0,0,0]
dir_vector=[1,1,0]
length=8
steps=10
line = create_line(center, dir_vector, length, steps)
v1=[0,1,0]
v2=[1,0,0]
l1=8
l2=8
steps=10
paral = create_paralelogram(center, v1, v2, l1, l2, steps)
normal_vector=[0,0,1]
radius=8
steps=10
polygon = create_polygon(center, normal_vector, radius, steps)

# Generamos grafica con circulo y elipses
plt.plot(line[:,0],line[:,1],'o', linewidth=2.0)
plt.plot(paral[:,0],paral[:,1], linewidth=2.0)
plt.plot(polygon[:,0],polygon[:,1], linewidth=2.0)
limitplot=8
plt.ylim(top = limitplot, bottom = -limitplot)
plt.xlim(left = limitplot, right = -limitplot)
plt.xticks(fontsize= 15)
plt.yticks(fontsize= 15)
plt.tight_layout()
plt.show()
