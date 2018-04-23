#Visual5_________________________Graphics CAP3
#Programacion de metodos numericos y Visual python
import pylab
#from numpy import linspace,sin  #sin de numpy es version para arreglos

#Graficas lineales
"""
x = [0.5,1.0,2.0,4.0,7.0,10.0]
y = [1.0,2.4,1.7,0.3,0.6,1.8]
pylab.plot(x,y)
pylab.show()

"""

#x =linspace(-10,10,100)  # del cero al 10 partido en 100//en arreglos
#y = sin(x)
#pylab.plot(x,y)
#pylab.show()


#____________________-cargando un archivo
from numpy import loadtxt

data = loadtxt("values.txt",float)
xx= data[:,0]
yy= data[:,1]
pylab.plot(xx,yy)
pylab.show()

#_____________________________________esto escribe uno a uno cada valor y prevee cualquier error antes de show
#from pylab import plot,show
from math import sin
from numpy import linspace

xpoints = []
ypoints = []
for x in linspace(0,10,100):
    xpoints.append(x)
    ypoints.append(sin(x))
pylab.plot(xpoints,ypoints)
pylab.show()

