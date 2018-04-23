#________________________WAVE INTERFERENCE
#VISUAL7 PYLAB CHAPTER 3

from math import sqrt, sin, pi
from numpy import empty
from pylab import imshow,gray,show

longitud_onda = 5.0
k = 2*pi/longitud_onda
xi0 = 1.0
separacion = 20.0  # separacion del centro en cm
lado = 100.0  # lado del cuadrado in cm
puntos = 500  # numero de grids a lo largo de cada lado
espaciado = lado/puntos

#calcular las posiciones del centro de los circulos 
x1 = lado/2 + separacion/2
y1= lado/2
x2= lado/2 - separacion/2
y2 = lado/2

#hacer un arreglo para guardar las alturas
xi = empty([puntos,puntos],float)

#calcular los valores en el arreglo
for i in range(puntos):
    y = espaciado*i
    for j in range(puntos):
        x = espaciado*j
        r1= sqrt((x-x1)**2+(y-y1)**2)
        r2= sqrt((x-x2)**2+(y-y2)**2)
        xi[i,j]=xi0*sin(k*r1)+xi0*sin(k*r2)

#plotear en pantalla
imshow(xi,origin="lower",extent=[0,lado,0,lado]) #permite ver un amplio rango en pantalla
gray()
show()
"""
Patron de interferencia: Muestra la superposicion de dos sets de ondas senoidales, creando una interferencia que
congelando parece q las barras grises  radian desde el centro del heat map.
"""